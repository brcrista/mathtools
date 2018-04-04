.PHONY: all tests typecheck wheel

all: typecheck tests wheel

typecheck:
	mypy mathtools --strict
	mypy tests --ignore-missing-imports --strict

tests:
	pytest --doctest-modules

wheel:
	python setup.py bdist_wheel
