#!/bin/sh

python manage.py migrate
python manage.py collectstatic --no-input
python manage.py search_index --rebuild
python -m celery -A toolbox worker -l info &
python -m celery -A toolbox beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler &
gunicorn --bind 0.0.0.0:8000 --threads 4 toolbox.wsgi:application