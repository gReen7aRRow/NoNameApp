run:
	python3 manage.py runserver
makemigrations:
	python3 manage.py makemigrations
migrate:
	python3 manage.py migrate
static:
	python3 manage.py collectstatic
lint:
	flake8 django_app apps

.PHONY: run makemigrations migrate static lint
