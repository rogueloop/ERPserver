#!/bin/bash
docker stop erpbackend_app || true
docker rm -f erpbackend_app || true
docker build --rm  -t erpbackend_app:ctrl .
docker run -d -p 8000:8000 erpbackend_app:ctrl