#!/usr/bin/env bash
# exit on error
set -o errexit

# poetry install
pip install -r requirements.txt

python manage.py makemigrations administracionProyecto
python manage.py makemigrations login
python manage.py makemigrations auth
python manage.py migrate
python manage.py collectstatic --no-input