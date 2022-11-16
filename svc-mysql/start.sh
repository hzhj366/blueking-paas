#!/usr/bin/env bash
# Exit on error
set -e

python manage.py migrate --no-input
python manage.py collectstatic --no-input

# load fixtures
# python manage.py loaddata data/fixtures/services.json
# python manage.py loaddata data/fixtures/plans.json

## Run!
command="gunicorn svc_mysql.wsgi -w 4 -b [::]:5000 -k gevent --max-requests 2048 --access-logfile '-' --access-logformat '%(h)s %(l)s %(u)s %(t)s \"%(r)s\" %(s)s %(b)s \"%(f)s\" \"%(a)s\" in %(L)s seconds' --log-level INFO --log-file=-"
exec bash -c "$command"