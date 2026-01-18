# Developer Guide

## Requirements
- Python 3.9+
- uv

## Setup
```bash
uv venv
uv sync --dev
```

## Common commands
```bash
# Run the app
uv run python search_engine.py "Chicken Breast" --limit 2

# Run tests
uv run pytest

# Run tests with testmon (incremental)
uv run pytest --testmon

# Watch tests (rerun on changes)
uv run pytest --testmon --testmon-noselect --looponfail

# Lint and format
uv run ruff check .
uv run ruff format .
```

## VS Code
- Use the Run panel: `Search Engine (debug)` or `Search Engine (run)`.
- Tasks: `uv: sync`, `uv: run search_engine`, `uv: test (pytest)`, `uv: testmon (watch)`.

## Makefile
```bash
make sync
make run
make test
make testmon
make lint
make fmt
```
