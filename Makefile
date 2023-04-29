.PHONY: test mypy format clean

clean:
	@rm -rf .mypy_cache/ .pytest_cache/ __pycache__/
	@poetry run coverage erase

format:
	@poetry run black .

mypy:
	@poetry run mypy .

precommit:
	@poetry run pre-commit install
	@poetry run pre-commit run --all-files

test:
	@poetry run coverage erase
	@poetry run coverage run --branch -m pytest tests/
	@poetry run coverage report --show-missing --fail-under=100 --skip-covered --skip-empty
