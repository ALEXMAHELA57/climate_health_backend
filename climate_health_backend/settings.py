import os
from pathlib import Path

# ----------------------------------
# BASE PROJECT CONFIGURATION
# ----------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-CHANGE_THIS_KEY_FOR_PRODUCTION'

DEBUG = True  # Set to False when deploying

ALLOWED_HOSTS = ['*']  # Change * to your domain later


# ----------------------------------
# INSTALLED APPS
# ----------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',  # your main app
]


# ----------------------------------
# MIDDLEWARE
# ----------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # for static files in production
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ----------------------------------
# URL CONFIGURATION
# ----------------------------------
ROOT_URLCONF = 'climate_health_backend.urls'


# ----------------------------------
# TEMPLATES (for React frontend integration)
# ----------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # where React build will go
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ----------------------------------
# WSGI APPLICATION
# ----------------------------------
WSGI_APPLICATION = 'climate_health_backend.wsgi.application'


# ----------------------------------
# DATABASE (SQLite by default)
# ----------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ----------------------------------
# PASSWORD VALIDATION
# ----------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


# ----------------------------------
# INTERNATIONALIZATION
# ----------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Nairobi'
USE_I18N = True
USE_TZ = True


# ----------------------------------
# STATIC FILES (for Django & React)
# ----------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# ----------------------------------
# DEFAULT PRIMARY KEY FIELD TYPE
# ----------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
