import os
import sys

BASE_DIR = '/app/'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]


ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_TZ = True

DATE_FORMAT = 'd.m.Y'
DATETIME_FORMAT = 'd.m.Y H:i'
TIME_FORMAT = 'H:i'

MEDIA_ROOT = os.path.join(BASE_DIR, 'images')
MEDIA_URL = '/images/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

SECRET_KEY = os.environ.get("SECRET_KEY")

DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.postgresql_psycopg2',
        "NAME": 'postgres',
        "USER": 'postgres',
        "PASSWORD": 'postgres',
        "HOST": 'postgres',
        "PORT": '5432',
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


APP_NAME = 'Food API'
DEBUG = os.getenv("DEBUG", 'False').lower() in ['true', '1']

INSTALLED_APPS += [
    ]


ALLOWED_HOSTS = ['*']



