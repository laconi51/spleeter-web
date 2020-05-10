#!/bin/bash

# Collect static files
# echo "Collect static files"
# python manage.py collectstatic --noinput

# Apply database migrations
echo "Waiting for postgres..."
while ! nc -z db 5432; do
    sleep 0.1
done
echo "PostgreSQL started"

echo "Apply database migrations"
# python manage.py flush --no-input
python manage.py migrate

# Start server
echo "Starting server"
npm run dev
