#!/usr/bin/env bash
# exit on error
set -o errexit

# poetry install
pip install -r requirements.txt

python manage.py migrate administracionProyecto
python manage.py migrate login
python manage.py migrate auth
python manage.py migrate
python manage.py collectstatic --no-input