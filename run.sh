#!/bin/bash
mkdir -p logs
poetry add coreapi
pip install coreapi
poetry shell
poetry install
poetry run python manage.py runserver 0.0.0.0:8000 >> logs/erp.log 2>&1 </dev/null