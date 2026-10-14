#!/usr/bin/env python3
"""Scan and bump the published Wiki CLI pins held by this monorepo.

The pins this repo carries, and where they live (the `Downstream templates`
rule in wazootech/wiki's AGENTS.md is what this automates):

  templates/**/.github/workflows/*.yml   wazootech-wiki==<version>  (PyPI)
  templates/**/deno.json                 jsr:@wazoo/wiki@<version>  (JSR)
  templates/**/*.md                      the same two syntaxes, in prose

The monorepo's own `.github/workflows/*.yml` installs the same CLI, so it is
scanned too: pinning the templates newer than the engine the repository's CI
installs would validate templates against a stale engine.

Markdown is in scope because a template's README repeats the install pin in
prose (`pip install wazootech-wiki==<version>`); a bump that leaves that
behind is the same stale pin in a second language. Only the two pin syntaxes
above are ever rewritten, and `assert-diff` fails if a bump changes anything
else on a line.

Subcommands
  scan          read-only report: every pin, every published version, any drift
  sync          rewrite the pins that are behind the published latest version
  check         exit 1 when a pin is behind the published latest version
  assert-diff   fail unless the git diff only changes version substrings

`sync` never downgrades: a pin ahead of the published latest (bumped by hand
before publishing) is reported and left alone.

Stdlib only, so the workflow needs no extra dependency.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

PYPI_PACKAGE = "wazootech-wiki"
JSR_PACKAGE = "@wazoo/wiki"
PYPI_URL = f"https://pypi.org/pypi/{PYPI_PACKAGE}/json"
JSR_URL = "https://jsr.io/@wazoo/wiki/meta.json"

# A version starts with a digit and ends at a quote, space, or '/' (the JSR pin
# is also used with a subpath: jsr:@wazoo/wiki@0.6.0/theme).
VERSION = r"[0-9][0-9A-Za-z.\-+]*"

# (label, registry, pattern) for every pin syntax the scanner understands.
PIN_PATTERNS = (
    (
        f"{PYPI_PACKAGE}==",
        "pypi",
        re.compile(rf"(?P<package>{re.escape(PYPI_PACKAGE)}==)(?P<version>{VERSION})"),
    ),
    (
        f"jsr:{JSR_PACKAGE}@",
        "jsr",
        re.compile(rf"(?P<package>jsr:{re.escape(JSR_PACKAGE)}@)(?P<version>{VERSION})"),
    ),
)

MASKED = "\u00abversion\u00bb"

# Generated trees that must never be scanned or rewritten.
EXCLUDED_PARTS = {".git", "node_modules", "_site", "dist", "build", "vendor"}


def version_key(version: str) -> tuple:
    """Order versions: numeric release first, pre-release after it."""
    core, _, pre = version.partition("-")
    numbers = []
    for part in core.split("."):
        digits = re.match(r"\d+", part)
        numbers.append(int(digits.group()) if digits else 0)
    while len(numbers) < 3:
        numbers.append(0)
    return (tuple(numbers), 0 if pre else 1, pre)


# ------------------------------------------------------------------- registry


def get_json(url: str) -> dict:
    last: Exception | None = None
    for attempt in (1, 2, 3):
        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": "wiki-templates pin bump (github.com/wazootech/wiki-templates)",
                "Accept": "application/json",
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                return json.loads(response.read().decode("utf-8"))
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            last = exc
            if attempt < 3:
                time.sleep(2 * attempt)
    raise SystemExit(f"error: could not read {url}: {last}")


def latest_pypi() -> str:
    """Latest published version on PyPI (info.version skips pre-releases)."""
    version = get_json(PYPI_URL).get("info", {}).get("version")
    if not version:
        raise SystemExit(f"error: no info.version in {PYPI_URL}")
    return version


def latest_jsr() -> str:
    """Latest published version on JSR (meta.json 'latest')."""
    version = get_json(JSR_URL).get("latest")
    if not version:
        raise SystemExit(f"error: no latest in {JSR_URL}")
    return version


# ------------------------------------------------------------------ discovery


def find_root(start: Path) -> Path:
    for candidate in [start, *start.parents]:
        if (candidate / "templates").is_dir() and (candidate / ".github").is_dir():
            return candidate
    raise SystemExit(f"error: no repository root above {start}")


def managed_sources(root: Path) -> list[Path]:
    """Markdown files this job may rewrite, skipping generated trees."""
    return sorted(
        p for p in root.rglob("*.md") if not EXCLUDED_PARTS.intersection(p.parts)
    )


def in_scope_files(root: Path) -> tuple[list[Path], list[Path]]:
    """Return (template files, monorepo files) whose pins this job manages."""
    templates = root / "templates"
    template_files: list[Path] = []
    for template in sorted(templates.glob("*")):
        workflows = template / ".github" / "workflows"
        if workflows.is_dir():
            template_files.extend(
                sorted(p for p in workflows.iterdir() if p.suffix in {".yml", ".yaml"})
            )
    template_files.extend(sorted(templates.rglob("deno.json")))
    template_files.extend(managed_sources(templates))
    monorepo_files = sorted(
        p
        for p in (root / ".github" / "workflows").iterdir()
        if p.suffix in {".yml", ".yaml"}
    )
    monorepo_files.extend(sorted(root.glob("*.md")))
    return template_files, monorepo_files


def template_name(root: Path, path: Path) -> str:
    parts = path.relative_to(root).parts
    return parts[1] if len(parts) > 2 and parts[0] == "templates" else "(monorepo)"


def pins_in(path: Path) -> list[dict]:
    """Every pin occurrence in one file, in file order."""
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return []
    found = []
    for index, line in enumerate(text.splitlines(), start=1):
        for label, registry, pattern in PIN_PATTERNS:
            for match in pattern.finditer(line):
                found.append(
                    {
                        "label": label,
                        "registry": registry,
                        "version": match.group("version"),
                        "line": index,
                        "span": match.span("version"),
                    }
                )
    return found


def collect(root: Path) -> dict:
    """Scan the in-scope files, plus every other file that carries a pin."""
    template_files, monorepo_files = in_scope_files(root)
    entries = []
    for group, files in (("templates", template_files), ("monorepo", monorepo_files)):
        for path in files:
            for pin in pins_in(path):
                entries.append({**pin, "group": group, "path": path})

    scope = {*template_files, *monorepo_files}
    outside = []
    for path in sorted((root / "templates").rglob("*")):
        if (
            not path.is_file()
            or path in scope
            or EXCLUDED_PARTS.intersection(path.parts)
        ):
            continue
        for pin in pins_in(path):
            outside.append({**pin, "path": path})
    return {"entries": entries, "outside": outside}


def summarize(root: Path, entries: list[dict]) -> dict:
    """Per-syntax, per-scope counts, plus a per-template PyPI breakdown."""
    counts = {}
    for label, registry, _ in PIN_PATTERNS:
        rows = [e for e in entries if e["label"] == label]
        groups = {}
        for group in ("templates", "monorepo"):
            scoped = [e for e in rows if e["group"] == group]
            groups[group] = {
                "occurrences": len(scoped),
                "files": len({e["path"] for e in scoped}),
                "templates": len(
                    {template_name(root, e["path"]) for e in scoped}
                    if group == "templates"
                    else set()
                ),
                "versions": sorted({e["version"] for e in scoped}),
            }
        counts[label] = {"registry": registry, "groups": groups}

    pypi_label = f"{PYPI_PACKAGE}=="
    per_template: dict[str, dict] = {}
    for entry in entries:
        if entry["label"] != pypi_label or entry["group"] != "templates":
            continue
        row = per_template.setdefault(
            template_name(root, entry["path"]), {"files": set(), "occurrences": 0}
        )
        row["files"].add(entry["path"])
        row["occurrences"] += 1
    counts[pypi_label]["per_template"] = {
        name: {"files": len(row["files"]), "occurrences": row["occurrences"]}
        for name, row in sorted(per_template.items())
    }
    return counts


# ---------------------------------------------------------------------- apply


def apply_versions(entries: list[dict], latest: dict) -> tuple[list, list]:
    """Rewrite pins behind the published latest; return (bumped, ahead)."""
    bumped, ahead = [], []
    for entry in entries:
        target = latest.get(entry["registry"])
        if not target or entry["version"] == target:
            continue
        if version_key(entry["version"]) > version_key(target):
            ahead.append(entry)
            continue
        entry["target"] = target
        bumped.append(entry)

    by_file: dict[Path, list[dict]] = {}
    for entry in bumped:
        by_file.setdefault(entry["path"], []).append(entry)

    for path, rows in by_file.items():
        lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
        # Apply edits last-to-first so the earlier spans stay valid.
        edits = sorted(
            (row["line"] - 1, row["span"][0], row["span"][1], row["target"]) for row in rows
        )
        for line_index, start, end, replacement in reversed(edits):
            line = lines[line_index]
            lines[line_index] = line[:start] + replacement + line[end:]
        path.write_text("".join(lines), encoding="utf-8")
    return bumped, ahead


def mask(line: str) -> str:
    """Blank out pin versions so two lines can be compared structurally."""
    for _, _, pattern in PIN_PATTERNS:
        line = pattern.sub(lambda m: m.group("package") + MASKED, line)
    return line


def diff_lines(root: Path) -> tuple[list[str], list[str]]:
    """Removed and added lines of the working-tree diff, ignoring hunks."""
    result = subprocess.run(
        ["git", "diff", "-U0"],
        cwd=root,
        capture_output=True,
        text=True,
        check=True,
    )
    removed, added = [], []
    for line in result.stdout.splitlines():
        if line.startswith("---") or line.startswith("+++"):
            continue
        if line.startswith("-"):
            removed.append(line[1:])
        elif line.startswith("+"):
            added.append(line[1:])
    return removed, added


def assert_diff(root: Path) -> bool:
    removed, added = diff_lines(root)
    if not removed and not added:
        print("assert-diff: working tree is clean.")
        return True
    if sorted(mask(line) for line in removed) != sorted(mask(line) for line in added):
        print("assert-diff: FAIL - the diff changes more than pin versions:")
        for line in sorted(set(removed + added)):
            print(f"  {line}")
        return False
    print(f"assert-diff: ok - {len(added)} changed line(s), version substrings only.")
    return True


# --------------------------------------------------------------------- output


def plural(count: int, noun: str) -> str:
    return f"{count} {noun}" if count == 1 else f"{count} {noun}s"


def report(root: Path, data: dict, latest: dict, drift: dict) -> None:
    counts = summarize(root, data["entries"])
    print("Pins found in scope")
    for label, registry, _ in PIN_PATTERNS:
        print(f"\n  {label}  ({registry})")
        for group in ("templates", "monorepo"):
            scoped = counts[label]["groups"][group]
            if not scoped["occurrences"]:
                continue
            where = (
                f"{plural(scoped['templates'], 'template')}, {plural(scoped['files'], 'file')}"
                if group == "templates"
                else f"{plural(scoped['files'], 'file')} in the monorepo's own workflows"
            )
            print(f"    {where}: {plural(scoped['occurrences'], 'occurrence')}")
            print(f"    pinned versions: {', '.join(scoped['versions'])}")

    per_template = counts[f"{PYPI_PACKAGE}=="]["per_template"]
    if per_template:
        print("\n  Per template (only the pins this job manages)")
        for name, row in per_template.items():
            print(
                f"    {name}: {plural(row['files'], 'file')}, "
                f"{plural(row['occurrences'], 'occurrence')}"
            )

    print("\nPublished latest")
    for registry, version in sorted(latest.items()):
        print(f"  {registry}: {version}")
    if not latest:
        print("  (offline: registry lookups skipped)")

    if not latest:
        print("\nDrift: unknown (registry lookups skipped).")
    elif drift["behind"]:
        print("\nDrift")
        for label, versions in drift["behind"].items():
            print(f"  {label} pinned at {', '.join(versions)}")
    else:
        print("\nDrift: none - every pin matches the published latest.")
    for label, versions in drift["ahead"].items():
        print(
            f"Note: {label} is pinned ahead of the published latest "
            f"({', '.join(versions)}); a manual bump, left alone."
        )

    if data["outside"]:
        print("\nPins outside the managed set (reported, never edited):")
        for entry in data["outside"]:
            path = entry["path"].relative_to(root).as_posix()
            print(f"  {path}:{entry['line']}: {entry['version']}")


def gh_output(values: dict, path: Path | None) -> None:
    if not path:
        return
    with open(path, "a", encoding="utf-8") as handle:
        for key, value in values.items():
            handle.write(f"{key}={value}\n")


def summary_markdown(root: Path, bumped: list[dict], latest: dict) -> str:
    """The PR body's version table (written outside the repo working tree)."""
    lines = [
        "### Pin bumps",
        "",
        "| Pin | Published latest | Occurrences |",
        "|-----|------------------|-------------|",
    ]
    for label, registry, _ in PIN_PATTERNS:
        rows = [row for row in bumped if row["label"] == label]
        if not rows:
            continue
        froms = ", ".join(sorted({row["version"] for row in rows}))
        lines.append(f"| `{label}` | {froms} -> {latest[registry]} | {len(rows)} |")
    lines += ["", "Files touched:", ""]
    for path in sorted({row["path"] for row in bumped}):
        rows = [row for row in bumped if row["path"] == path]
        targets = ", ".join(sorted({row["target"] for row in rows}))
        lines.append(f"- `{path.relative_to(root).as_posix()}` -> `{targets}`")
    return "\n".join(lines) + "\n"


def drift_of(entries: list[dict], latest: dict) -> dict:
    drift: dict[str, dict] = {"behind": {}, "ahead": {}}
    for label, registry, _ in PIN_PATTERNS:
        target = latest.get(registry)
        if not target:
            continue
        versions = sorted({e["version"] for e in entries if e["label"] == label})
        behind = [v for v in versions if version_key(v) < version_key(target)]
        ahead = [v for v in versions if version_key(v) > version_key(target)]
        if behind:
            drift["behind"][label] = behind
        if ahead:
            drift["ahead"][label] = ahead
    return drift


# ----------------------------------------------------------------------- main


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "command", choices=["scan", "sync", "check", "assert-diff"], help="what to do"
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help="repository root (default: discovered above this script)",
    )
    parser.add_argument(
        "--offline", action="store_true", help="skip registry lookups; report pins only"
    )
    parser.add_argument(
        "--summary-file",
        type=Path,
        default=None,
        help="write the PR body section for sync here (keep it outside the repo)",
    )
    parser.add_argument(
        "--github-output",
        type=Path,
        default=None,
        help="append step outputs (changed, latest_pypi, latest_jsr) to this file",
    )
    args = parser.parse_args(argv)

    root = (args.root or find_root(Path(__file__).resolve().parent)).resolve()

    if args.command == "assert-diff":
        return 0 if assert_diff(root) else 1

    data = collect(root)
    latest = {}
    if args.offline:
        print("offline: registry lookups skipped, published versions unknown")
    else:
        latest = {"pypi": latest_pypi(), "jsr": latest_jsr()}
    drift = drift_of(data["entries"], latest)

    if args.command == "scan":
        report(root, data, latest, drift)
        gh_output(
            {
                "changed": "unknown",
                "drift": "true" if drift["behind"] else "false",
                "latest_pypi": latest.get("pypi", ""),
                "latest_jsr": latest.get("jsr", ""),
            },
            args.github_output,
        )
        return 0

    if args.command == "check":
        if not drift["behind"]:
            print("check: every pin matches the published latest.")
            return 0
        for label, versions in drift["behind"].items():
            print(f"check: {label} pinned at {', '.join(versions)}")
        return 1

    # sync
    bumped, ahead = apply_versions(data["entries"], latest)
    if not bumped:
        print("sync: no pin is behind the published latest; nothing changed.")
        for label, versions in drift["ahead"].items():
            print(f"sync: {label} pinned ahead ({', '.join(versions)}); left alone")
        gh_output(
            {
                "changed": "false",
                "latest_pypi": latest.get("pypi", ""),
                "latest_jsr": latest.get("jsr", ""),
            },
            args.github_output,
        )
        return 0

    print(f"sync: bumped {len(bumped)} pin(s).")
    for row in bumped:
        print(
            f"  {row['path'].relative_to(root).as_posix()}:{row['line']} "
            f"{row['version']} -> {row['target']}"
        )
    if args.summary_file:
        args.summary_file.write_text(
            summary_markdown(root, bumped, latest), encoding="utf-8"
        )
    gh_output(
        {
            "changed": "true",
            "latest_pypi": latest.get("pypi", ""),
            "latest_jsr": latest.get("jsr", ""),
        },
        args.github_output,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
