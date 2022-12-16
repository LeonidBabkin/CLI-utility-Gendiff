build:
	poetry build

install:
	poetry install

reinstall:
	pip install --user --force-reinstall dist/*.whl

start:
	gendiff tests/fixtures/file1.json tests/fixtures/file2.json

lint:
	poetry run flake8 gendiff

test:  
	poetry run coverage run --source=tests -m pytest tests

cc-cover:
	poetry run coverage xml

report-coverage:
	poetry run coverage report

.PHONY: build install reinstall start lint test report-coverage
