# #!/usr/bin/env bash
# set -euxo pipefail

# mypy --disallow-untyped-defs --ignore-missing-imports /code/api/
isort --multi-line=3 --trailing-comma --force-grid-wrap=0 --use-parentheses --line-width=79 --check --diff /code/api/
black --check -l 79 /code/api/
# E712 added here, because of endless (DB row == True) comparisons in code
flake8 /code/api/ --max-line 79 --ignore F403,F401,W503,E203,E711,E712,B008,N805,N817
bandit -r /code/api/
