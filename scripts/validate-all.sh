#!/usr/bin/env bash
set -u

failed=0
count=0

for cfg in templates/*/wiki.yml templates/*/docs/wiki.yml templates/*/sample/wiki.yml; do
  [ -f "$cfg" ] || continue
  tpl="${cfg#templates/}"; tpl="${tpl%%/*}"
  count=$((count + 1))
  echo "=== $tpl ($cfg) ==="
  wiki -c "$cfg" fmt --check       || failed=1
  wiki -c "$cfg" lint --strict -v  || failed=1
  wiki -c "$cfg" check --strict -v || failed=1
  wiki -c "$cfg" render --check -v || failed=1
done

if [ "$count" -eq 0 ]; then
  echo "ERROR: no template configs found."
  exit 1
fi

if [ "$failed" -ne 0 ]; then
  echo "ERROR: one or more templates failed validation."
  exit 1
fi

echo "All $count templates validated."
