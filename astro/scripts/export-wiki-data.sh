#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
wiki -c "${ROOT}/wiki.yaml" check --strict
wiki -c "${ROOT}/wiki.yaml" export -f json-ld -o "${ROOT}/web/data/wiki-export.json"
