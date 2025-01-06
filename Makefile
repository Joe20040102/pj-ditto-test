.PHONY: lint
lint:
	poetry run isort .
	poetry run black .
	poetry run flake8 --exclude .venv,.git,__pycache__ --ignore=E203,E501,W503 .

.PHONY: run
run:
	poetry run uvicorn app.main:app --reload