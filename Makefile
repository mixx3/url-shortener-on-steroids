APPLICATION_NAME = url_shortener
args := $(wordlist 2, 100, $(MAKECMDGOALS))


db:
	docker-compose -f docker-compose.yml up -d --remove-orphans

run:
	poetry run python3 -m $(APPLICATION_NAME)

migrate:
	poetry run alembic upgrade $(args)

alembic_review:
	poetry run alembic revision --autogenerate -m $(args)

black:
	poetry run black $(APPLICATION_NAME)
