#!/bin/bash
set -eu

mkdir -p ${APP_ROOT}/tmp/uvicorn_sockets

# Run FastAPI application
poetry run alembic upgrade head
poetry run gunicorn main:app --worker-class uvicorn.workers.UvicornWorker --bind=unix://${APP_ROOT}/tmp/uvicorn_sockets/uvicorn.sock

exec "$@"
