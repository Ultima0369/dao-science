# Project Dao.Science — standard development commands
.PHONY: help install sync build serve test lint audit clean

help:
	@echo "Available targets:"
	@echo "  install   Install core, simulation, and dev dependencies"
	@echo "  sync      Sync docs/ mirror from repository root"
	@echo "  build     Build MkDocs site (strict)"
	@echo "  serve     Serve MkDocs site locally"
	@echo "  test      Run pytest suite"
	@echo "  lint      Run ruff linter"
	@echo "  typecheck Run mypy type checker"
	@echo "  audit     Run all audit scripts"
	@echo "  clean     Remove generated docs/, site/, and simulation outputs"

install:
	pip install -r requirements.txt
	pip install -r simulations/requirements.txt
	pip install -r tools/n_of_1/requirements.txt
	pip install -e .
	pip install pytest ruff mypy

sync:
	python scripts/sync_docs.py

build: sync
	mkdocs build --strict

serve: sync
	mkdocs serve

test:
	pytest -q

lint:
	ruff check scripts tests simulations tools src

typecheck:
	mypy src tests scripts tools/n_of_1/scripts

audit:
	python scripts/audit_links.py
	python scripts/audit_nav_coverage.py
	python scripts/audit_math_delimiters.py
	python scripts/audit_consistency.py

clean:
	python scripts/sync_docs.py
	rm -rf site
	rm -f simulations/*.png simulations/*.csv
	rm -rf simulations/__pycache__
	rm -rf tests/__pycache__
	rm -rf scripts/__pycache__
	rm -rf tools/__pycache__ tools/*/__pycache__
