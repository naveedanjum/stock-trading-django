#!/bin/sh

# Exit immediately if a command exits with a non-zero status.
set -e

# Run database migrations
echo "Running database migrations..."
python manage.py migrate --noinput

# Optionally, run your custom command to generate fake data
# Uncomment the next line if you want to generate fake data every time the container starts
# python manage.py generate_fake_data --companies 40 --days 30

# Start gunicorn
echo "Starting gunicorn..."
exec gunicorn --bind 0.0.0.0:8000 investment_site.wsgi:application
