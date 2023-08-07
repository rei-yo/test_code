#!/bin/bash
python manage.py makemigrations accounts
python manage.py migrate accounts
python manage.py makemigrations nuxtapi
python manage.py migrate nuxtapi


