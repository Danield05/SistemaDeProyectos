#!/usr/bin/env bash
# exit on error
set -o errexit

# poetry install
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# Crear superusuario inicialmente
python manage.py shell < create_superuser.py