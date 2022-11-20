APPLICATION_NAME = bookmarker

run:
	poetry run python3 -m $(APPLICATION_NAME)

migrate:
	cd $(APPLICATION_NAME)/db && poetry run alembic upgrade $(args)