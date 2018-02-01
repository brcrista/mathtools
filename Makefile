.PHONY: all tests typecheck

all: typecheck tests

typecheck:
	mypy mathtools
	mypy tests --ignore-missing-imports

tests:
	pytest --doctest-modules