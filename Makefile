.PHONY: install test lint format typecheck check clean

install:
	uv sync

test:
	uv run coverage erase
	uv run coverage run --branch -m pytest tests/
	uv run coverage report --show-missing --fail-under=100

lint:
	uv run ruff check .

format:
	uv run ruff format .

typecheck:
	uv run ty check src/pyosrs/

check: lint typecheck test

clean:
	rm -rf .pytest_cache/ .coverage src/__pycache__/ dist/ .ruff_cache/
