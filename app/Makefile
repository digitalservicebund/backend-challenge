.PHONY: test mypy lint clean dev install dist run run-docker backend-image help

PYTHONPATH=$(${PWD%/*})

help:
	@echo
	@echo "  test          run tests"
	@echo "  mypy          typecheck using mypy"
	@echo "  lint          lint project using flake8"
	@echo "  autoformat    autoformat files using black"
	@echo "  clean         remove build and python file artifacts"
	@echo "  dev           install in development mode"
	@echo "  install       install without dev dependencies"
	@echo "  dist          build dist packages"
	@echo "  run           run server for development"
	@echo "  run-docker    start Docker container"
	@echo "  backend-image build Docker image for backend"
	@echo "  help          print this message"
	@echo


ensure-poetry:
	@if ! [ -x $(command -v poetry) ]; then \
		echo "Please install poetry (e.g. pip install poetry)"; \
		exit 1; \
	fi

mypy: ensure-poetry
	poetry run mypy --strict app/

lint: ensure-poetry mypy
	poetry check
	poetry run flake8 app/ tests/

autoformat: ensure-poetry lint
	poetry run black app tests

test: ensure-poetry
	poetry run pytest --cov app/ --strict tests

clean:
	find . -name '*.pyc' -delete
	find . -name __pycache__ -delete
	rm -rf .coverage dist build *.egg-info

dist: ensure-poetry clean
	poetry build
	ls -l dist

dev: ensure-poetry clean
	poetry install

install: ensure-poetry clean
	poetry install --no-dev

run: ensure-poetry clean
	export PYTHONPATH=$${PWD%/*}; \
	poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

backend-image:
	docker build -t dsb-backend:0.1.0 . --no-cache

run-docker:
	docker run -p 8000:8000 --name dsb-backend dsb-backend