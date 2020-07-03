.PHONY: install test

default: test

install:
	pipenv install --dev --skip-lock

test:
	PYTHONPATH=./src pytest
	# python -m pytest

build:
	python setup.py bdist_wheel
