.PHONY: all tests typecheck

all: typecheck tests

typecheck:
	mypy mathtools --strict
	mypy tests --ignore-missing-imports --strict

tests:
	pytest --doctest-modules