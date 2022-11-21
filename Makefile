APPLICATION_NAME = url_shortener
args := $(wordlist 2, 100, $(MAKECMDGOALS))


run:
	poetry run python3 -m $(APPLICATION_NAME)

migrate:
	poetry run alembic upgrade $(args)

alembic_review:
	poetry run alembic revision --autogenerate -m $(args)
