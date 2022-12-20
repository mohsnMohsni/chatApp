# Chat App
Application to chat in async way.

[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

# core based on:
  - Python 3.10 version
  - Django 4.1 version
  - Channels 4.0 version

# Technologies are used:
  - Cache system
  - Redis db

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
