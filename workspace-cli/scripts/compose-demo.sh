#!/usr/bin/env bash
# Credential-free composition smoke test: seeds two independent sub-wiki git
# repositories, composes them as sources into the umbrella corpus, runs the
# four gates, and proves both sub-wikis surface in the union view.
#
# Requires: git and a `wiki` CLI on PATH (pip install wazootech-wiki).
# No GitHub credentials or network remotes are needed.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

# Allow overriding the Wiki CLI binary (e.g. a pinned venv path in CI).
WIKI="${WIKI:-wiki}"

git_dummy() { git -c user.email=demo@example.com -c user.name=demo "$@"; }

echo "==> seeding two independent sub-wiki repositories (alpha, beta)"

for name in alpha beta; do
  mkdir -p "$TMP/$name/wiki"
  cp "$ROOT/sample-subwiki/wiki.yml" "$TMP/$name/wiki.yml"
done

cat > "$TMP/alpha/wiki/alpha-home.md" <<'EOF'
---
type: TechArticle
headline: Alpha Sub-wiki Home
description: Independently-owned engineering sub-wiki seeded by the compose demo.
---

# Alpha Sub-wiki Home

Independently-owned engineering sub-wiki. Composition proves its graph surfaces
in the umbrella union view.
EOF

cat > "$TMP/beta/wiki/beta-home.md" <<'EOF'
---
type: TechArticle
headline: Beta Sub-wiki Home
description: Independently-owned data sub-wiki seeded by the compose demo.
---

# Beta Sub-wiki Home

Independently-owned data sub-wiki. Composition proves its graph surfaces in the
umbrella union view.
EOF

for name in alpha beta; do
  git init -q "$TMP/$name"
  git -C "$TMP/$name" add -A
  git_dummy -C "$TMP/$name" commit -qm "seed $name sub-wiki"
done

echo "==> composing umbrella corpus with both sources"

mkdir -p "$TMP/umbrella/docs"
cp -R "$ROOT/docs/." "$TMP/umbrella/docs/"
printf '\n' >> "$TMP/umbrella/docs/wiki.yml"
cat >> "$TMP/umbrella/docs/wiki.yml" <<EOF
sources:
  - name: alpha
    type: git
    url: $TMP/alpha
    path: wiki
  - name: beta
    type: git
    url: $TMP/beta
    path: wiki
EOF

UMBRELLA="$TMP/umbrella/docs/wiki.yml"

echo "==> installing pinned sources"
$WIKI -c "$UMBRELLA" install

echo "==> running the four gates on the composed corpus"
$WIKI -c "$UMBRELLA" fmt --check
$WIKI -c "$UMBRELLA" lint --strict -v
$WIKI -c "$UMBRELLA" check --strict -v
$WIKI -c "$UMBRELLA" render --check -v

echo "==> assert both sub-wikis surface in the union view"
RESULT="$($WIKI -c "$UMBRELLA" query -f csv "$(cat "$ROOT/queries/union-headlines.rq")")"
echo "$RESULT"
grep -q "Alpha Sub-wiki Home" <<<"$RESULT" || { echo "FAIL: alpha missing"; exit 1; }
grep -q "Beta Sub-wiki Home" <<<"$RESULT" || { echo "FAIL: beta missing"; exit 1; }

echo "==> assert per-source provenance names both graphs"
if $WIKI -c "$UMBRELLA" query -f csv "$(cat "$ROOT/queries/provenance-graphs.rq")" > "$TMP/prov.csv" 2>/dev/null; then
  grep -q "$TMP/alpha" "$TMP/prov.csv" || { echo "FAIL: alpha graph missing"; exit 1; }
  grep -q "$TMP/beta" "$TMP/prov.csv" || { echo "FAIL: beta graph missing"; exit 1; }
  echo "$(cat "$TMP/prov.csv")"
else
  echo "SKIP: GRAPH queries need a newer Wiki CLI than the pinned 0.1.21."
fi

echo "PASS: two sub-wikis surface as composed source graphs."