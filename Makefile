.PHONY: all
all: pip typecheck tests sdist wheel

.PHONY: clean
clean:
	rm -rf .mypy_cache build dist *.egg-info
	rm -rf **/__pycache__

.PHONY: pip
pip:
	pip install -r requirements.txt

.PHONY: typecheck
typecheck:
	mypy mathtools --strict
	mypy tests --ignore-missing-imports --strict

.PHONY: test
test:
	pytest --doctest-modules

.PHONY: sdist
sdist:
	python setup.py sdist

.PHONY: wheel
wheel:
	pip install wheel
	python setup.py bdist_wheel

.PHONY: upload
upload:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*