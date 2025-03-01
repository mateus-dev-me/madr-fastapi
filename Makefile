.ONESHELL:
ENV_PREFIX=$(shell python -c "if __import__('pathlib').Path('.venv/bin/pip').exists(): print('.venv/bin/')")
USING_POETRY=$(shell grep "tool.poetry" pyproject.toml && echo "yes")

.PHONY: help
help:             ## Show the help.
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@fgrep "##" Makefile | fgrep -v fgrep


.PHONY: run
run: test
	@$(ENV_PREFIX)python app/manage.py runserver


.PHONY: show
show:             ## Show the current environment.
	@echo "Current environment:"
	@if [ "$(USING_POETRY)" ]; then poetry env info && exit; fi
	@echo "Running using $(ENV_PREFIX)"
	@$(ENV_PREFIX)python -V
	@$(ENV_PREFIX)python -m site


.PHONY: install
install:          ## Install the project in dev mode.
	@if [ "$(USING_POETRY)" ]; then poetry install && exit; fi
	@echo "Don't forget to run 'make virtualenv' if you got errors."
	$(ENV_PREFIX)pip install -e .[test]


.PHONY: fmt
fmt:              ## Format code using ruff
	$(ENV_PREFIX)ruff format && ruff check --fix --unsafe-fixes


.PHONY: lint
lint:             ## Run pep8, black, mypy linters.
	$(ENV_PREFIX)ruff check


.PHONY: test
test: lint        ## Run tests and generate coverage report.
	$(ENV_PREFIX)pytest -v --cov=. -l --tb=short --maxfail=1
	$(ENV_PREFIX)coverage xml
	$(ENV_PREFIX)coverage html


.PHONY: clean
clean:            ## Clean unused files.
	@find . -name '*.pyc' -exec rm -rf {} \;
	@find . -name '*.pyc' -exec rm -rf {} \;
	@find . -name 'Thumbs.db' -exec rm -rf {} \;
	@find . -name '*~' -exec rm -rf {} \;
	rm -rf .cache
	rm -rf __pycache__
	rm -rf buildrm  
	rm -rf distrm  
	rm -rf *.egg-inform  
	rm -rf htmlcovrm  
	rm -rf .tox/rm  
	rm -rf docs/_build.PHONY: virtualenv


.PHONY: venv
venv:       ## Create a virtual environment.
	@if [ "$(USING_POETRY)" ]; then poetry install && exit; fi
	@echo "creating virtualenv ..."
	@rm -rf .venv
	@python3 -m venv .venv
	@./.venv/bin/pip install -U pip
	@./.venv/bin/pip install -e .[test]
	@echo
	@echo "!!! Please run 'source .venv/bin/activate' to enable the environment !!!"
