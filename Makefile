.PHONY: all
all: dependencies typecheck tests sdist wheel

.PHONY: clean
clean:
	rm -rf .mypy_cache build dist *.egg-info
	rm -rf **/__pycache__
	rm -rf junit/

.PHONY: dependencies
dependencies:
	pip install -r requirements-dev.txt

.PHONY: typecheck
typecheck:
	mypy mathtools --strict
	mypy tests --ignore-missing-imports --strict

.PHONY: tests
tests:
	pytest --doctest-modules --junitxml=junit/test-results.xml

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