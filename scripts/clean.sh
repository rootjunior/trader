# #!/usr/bin/env bash
# set -euo pipefail

isort --multi-line=3 --trailing-comma --force-grid-wrap=0 --use-parentheses --line-width=79 /code/api/
black /code/api/ -l 79

