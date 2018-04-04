.PHONY: all pip tests typecheck wheel

all: pip typecheck tests wheel

pip:
	pip install wheel
	pip install -r requirements.txt

typecheck:
	mypy mathtools --strict
	mypy tests --ignore-missing-imports --strict

tests:
	pytest --doctest-modules

wheel:
	python setup.py bdist_wheel
