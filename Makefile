.PHONY: install sync run test testmon lint fmt precommit-install precommit-run

install:
	uv sync --dev

sync:
	uv sync --dev

run:
	uv run python search_engine.py "Chicken Breast" --limit 2

test:
	uv run pytest

testmon:
	uv run pytest --testmon --testmon-noselect --looponfail

lint:
	uv run ruff check .

fmt:
	uv run ruff format .

precommit-install:
	uv run pre-commit install

precommit:
	uv run pre-commit run --all-files
