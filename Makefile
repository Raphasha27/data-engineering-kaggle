.PHONY: install install-dev lint test clean docker-build docker-run

install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"

lint:
	ruff check . --fix
	ruff format . --check

test:
	pytest tests/ -v --tb=short --cov=src --cov-report=term-missing

test-all:
	pytest tests/ -v --tb=short

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache .ruff_cache build dist *.egg-info

docker-build:
	docker compose build

docker-run:
	docker compose up

docker-down:
	docker compose down -v

security:
	bandit -r src/ -ll
	safety check --full-report

pre-commit:
	pre-commit run --all-files
