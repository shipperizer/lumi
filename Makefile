.PHONY: test run install help

PIP?=pip3
PYTEST?=py.test
PYTHON?=python3

install:
	$(PIP) install -r requirements.txt

test:
	$(PYTEST) test/

run:
	$(PYTHON) lumido.py

help:
	@printf "to launch the program use 'make run' or 'python lumido.py' \n"
	@printf "to setup more cronjobs add them to the 'conf' file \n"
	@printf "to install dependencies run 'make install' or use pip with the requirements file \n"
	@printf "to launch the tests just run 'make test' or 'py.test test'"
