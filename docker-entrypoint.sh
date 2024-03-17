#!/bin/sh

python manage.py makemigrations
python manage.py migrate
# python manage.py collectstatics --no-input
python -m celery -A toolbox worker -l info &
python -m celery -A toolbox beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler &
python manage.py runserver 0.0.0.0:8000