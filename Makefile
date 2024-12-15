.PHONY: setup test lint clean docs

setup:
	@echo "🚀 Setting up development environment..."
	bash setup_environment.sh

test:
	pytest tests/ -v

lint:
	black src/ tests/
	flake8 src/ tests/
	mypy src/ tests/

clean:
	rm -rf .venv build dist *.egg-info __pycache__ .pytest_cache .coverage

docs:
	sphinx-build docs docs/_build

check: lint test 