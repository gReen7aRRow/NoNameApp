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
celery:
	celery -A django_app worker -l info
flower:
	celery -A django_app flower

.PHONY: run makemigrations migrate static lint celery flower
