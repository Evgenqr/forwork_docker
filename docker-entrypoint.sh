#!/bin/bash

python manage.py migrate  --noinput
python manage.py createsuperuser --noinput --username admin --email admin@admin.com

python manage.py runserver 0.0.0.0:8000
