#!/bin/bash
docker stop erpbackend_app || true
docker rm -f erpbackend_app || true
docker build -t erpbackend_app .
docker run -p 8000:8000 -d --name erpbackend_app erpbackend_app
docker ps -a