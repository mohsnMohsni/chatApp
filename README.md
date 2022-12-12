# Core
Base config for django scale projects.

# core based on:
  - Python 3.10 version
  - Django 4.1 version

# Technologies are used:
  - Celery
  - REST api
  - Cache system
  - Test driven
  - Redis db
  - Kavenegar

# How to run it?

### install dependencies:

install redis

    sudo apt install redis-server

create virtualenv

    python3.10 -m venv venv

active virtualenv

    source venv/bin/activate

install packages

    pip install -r requirements/local.txt

    pip install -r requirements/production.txt

migrate migrations on db

    python manage.py migrate

run celery

    celery -A extensions worker -l DEBUG

    celery -A extensions beat -l DEBUG -S django

run test

    pytest

show tests functions

    pytest --collect-only

show test coverage

    pytest --cov

run server

    python manage.py runserver

    python manage.py runserver 0.0.0.0:8000
