# shop_compare
Scripts to try to compare prices across supermarket chains in the UK.

## Setup (uv)
Create a virtual environment and sync dependencies with uv:

```bash
uv venv
uv sync
```

## Quality
```bash
uv run ruff format .
uv run ruff check .
uv run pytest
```

## Run
Activate the environment (or use `uv run`) and run the script(s):

```bash
uv run python search_engine.py
```
