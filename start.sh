#!/usr/bin/env bash
set -e
exec gunicorn -w 4 -b 0.0.0.0:5000 simple_flask_api.app.run:app
