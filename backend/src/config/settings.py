# backend/src/config/settings.py

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', 'your-default-secret-key')

DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-party apps
    'rest_framework',
    # Your apps
    'simulation',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # ... other middleware
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # ... context processors
            ],
        },
    },
]

WSGI_APPLICATION = 'app.application'

# backend/src/config/settings.py

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}


# Database


# backend/src/config/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': os.getenv('POSTGRES_DB', 'human_digital_twin'),
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': 'db',
            'port': 5432,
            'username': os.getenv('POSTGRES_USER', 'yourusername'),
            'password': os.getenv('POSTGRES_PASSWORD', 'yourpassword'),
            'authSource': 'admin',
            'authMechanism': 'SCRAM-SHA-256',
        }
    },
    'mongo': {
        'ENGINE': 'djongo',
        'NAME': 'human_digital_twin_mongo',
        'CLIENT': {
            'host': 'mongo',
            'port': 27017,
            'username': 'mongouser',
            'password': 'mongopassword',
            'authSource': 'admin',
            'authMechanism': 'SCRAM-SHA-256',
        }
    }
}


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
