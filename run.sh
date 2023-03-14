#!/bin/bash
cd erpbackend
mkdir -p logs
poetry shell
poetry install
poetry run python manage.py runserver 0.0.0.0:8000 >> logs/deepspeech.log 2>&1 </dev/null