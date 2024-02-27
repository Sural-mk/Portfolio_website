#!/usr/bin/env bash
#exit on error
set -o errexit 

pip install -r requirements.txt
python manage.py makemigrations 
python manage.py migrate
python manage.py create_super_user --username Suralmkoracle1313 --password oracle1313##