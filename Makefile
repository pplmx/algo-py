.PHONY: help install fmt lint test check

help: ## Show this help message
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "    %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

##@ Development

install: ## Install dependencies
	@uv pip sync

fmt: ## Format code using ruff
	@uv run ruff format .

lint: ## Lint code using ruff
	@uv run ruff check .

test: ## Run tests
	@uv run pytest

##@ Quality Assurance

check: lint test ## Run all checks
