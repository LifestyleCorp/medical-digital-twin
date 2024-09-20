#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "Deploying the Human Digital Twin project..."

# Pull the latest code
git pull origin main

# Build and run Docker containers
docker-compose up --build -d

echo "Deployment completed successfully."
