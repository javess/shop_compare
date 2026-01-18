# AGENTS

This repo favors clear developer ergonomics and documentation hygiene. When making changes:

## Tests
- Run unit tests with `uv run pytest`.
- For incremental runs, use `uv run pytest --testmon`.
- For watch mode, use `make testmon`.

## Lint, format, and static analysis
- Format: `uv run ruff format .`
- Lint: `uv run ruff check .`
- Pre-commit (recommended): `make precommit-install` once, then `make precommit-run` before pushing.

## Documentation
- Keep `README.md` and `DEVELOPMENT.md` accurate with any workflow or command changes.
- If you add new scripts, tasks, or env vars, document them.

## Docstrings
- Prefer docstrings on all public modules, classes, and functions.
- Use concise, Google-style docstrings, describing args/returns and side effects.
