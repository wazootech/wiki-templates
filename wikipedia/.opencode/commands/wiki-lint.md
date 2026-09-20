---
description: Run all wiki validation checks
---
Run the following verification checks on this wiki:
1. `git diff --check`
2. `wiki -c wiki.yml fmt --check`
3. `wiki -c wiki.yml lint --strict`
4. `wiki -c wiki.yml check --strict`
Report any failures with specific file paths and line numbers.
