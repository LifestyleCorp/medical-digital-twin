#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "Setting up the Human Digital Twin project..."

# Backend setup
echo "Setting up backend..."
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser --noinput || true
deactivate

# Frontend setup
echo "Setting up frontend..."
cd ../frontend
npm install

echo "Setup completed successfully."
