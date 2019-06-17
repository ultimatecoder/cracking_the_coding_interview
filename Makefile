test:
	pipenv run pytest solutions

lint:
	pipenv run flake8 solutions
	pipenv run mypy solutions
