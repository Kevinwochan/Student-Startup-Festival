#!/bin/sh

timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
echo "=== Updating SSF Repo: log entry $timestamp ==="
cd ~/Student-Startup-Festival;
git pull;
chown -R :www-data .
pipenv run python manage.py migrate --no-input
pipenv run python manage.py makemigrations --no-input
pipenv run python manage.py collectstatic --no-input --clear
echo "==========================="

