#!/bin/sh

# Run database migrations
python manage.py makemigrations --no-input
python manage.py migrate --no-input
# collect static files
python manage.py collectstatic --no-input

NAME=”BitcoinExchange” # Name of the application
NUM_WORKERS=3 # how many worker processes should Gunicorn spawn

MAX_REQUESTS=1 # reload the application server for each request

echo “Starting $NAME as `whoami` with Gunicorn.”

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use –daemon)
gunicorn bitcoin_rates.wsgi:application \
    --name $NAME \
    --workers $NUM_WORKERS \
    --max-requests $MAX_REQUESTS \
    --bind=0.0.0.0:8000 \
    --log-level=error \
    --access-logfile=logs/gunicorn-access \
    --error-logfile=logs/gunicorn-error \
    --daemon \


celery -A bitcoin_rates -l info worker -B
