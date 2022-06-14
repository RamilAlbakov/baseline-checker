install:
	poetry install

lint:
	poetry run flake8 baseline_checker

selfcheck:
	poetry check

check: selfcheck lint

build: check
	poetry build

isort:
	poetry run isort baseline_checker

.PHONY: install lint selfcheck check build isort