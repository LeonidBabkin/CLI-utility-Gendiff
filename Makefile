build:
	poetry build

reinstall:
	pip install --user --force-reinstall dist/*.whl

start:
	gendiff gendiff/fixtures/file1.json gendiff/fixtures/file2.json

lint:
	poetry run flake8 gendiff
