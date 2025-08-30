.PHONY: help install test test-cov run clean docker-build docker-run docker-test docker-stop

help: ## Show this help message
	@echo "ACEestFitness - Available Commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install production dependencies
	pip install -r requirements.txt

install-dev: ## Install development and test dependencies
	pip install -r requirements.txt
	pip install -r requirements-test.txt

test: ## Run tests
	pytest test_app.py -v

test-cov: ## Run tests with coverage
	pytest test_app.py -v --cov=app --cov-report=html --cov-report=term-missing

run: ## Run the Flask application
	python app.py

clean: ## Clean up generated files
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "htmlcov" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type f -name "workouts.json" -delete

docker-build: ## Build Docker image
	docker build -t aceest-fitness:latest .

docker-run: ## Run Docker container
	docker run -d -p 5000:5000 --name fitness-app aceest-fitness:latest

docker-test: ## Build and run test Docker image
	docker build -f Dockerfile.test -t aceest-fitness:test .
	docker run --rm aceest-fitness:test

docker-stop: ## Stop and remove Docker container
	docker stop fitness-app || true
	docker rm fitness-app || true

docker-compose-up: ## Start with Docker Compose
	docker-compose up --build

docker-compose-down: ## Stop Docker Compose
	docker-compose down

lint: ## Run code linting
	flake8 app.py test_app.py
	pylint app.py test_app.py

security: ## Run security checks
	bandit -r . -f json -o bandit-report.json
	safety check -r requirements.txt --json --output safety-report.json

all: install-dev test-cov docker-build docker-test ## Run all checks and tests 