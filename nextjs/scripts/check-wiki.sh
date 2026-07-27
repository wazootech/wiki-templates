#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
wiki -c "${ROOT}/wiki.yml" check --strict
wiki -c "${ROOT}/wiki.yml" lint --strict
