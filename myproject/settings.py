"""
Django settings for hotel project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

import socket

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mpxel*0sj*5u@c3q1=xm15q+k!8)(t9chj!pel0^=dv9+m-in('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hbooking',
)

'''
REVIEW_RATING_CHOICES = (
    ('1', 'bad'),
    ('2', 'average'),
    ('3', 'excellent'),
)
'''

#REVIEW_FORM_CHOICE_WIDGET = 'django.forms.widgets.RadioSelect'

#REVIEW_ALLOW_ANONYMOUS="True"

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'hotel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
		'django.core.context_processors.request',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'hotel.wsgi.application'

STAR_RATINGS_RERATE = True

STAR_RATINGS_ANONYMOUS = True

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

if socket.gethostname() == 'delevere-pc':
    DEBUG = TEMPLATE_DEBUG = True
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'naman',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',
	'OPTIONS': {
         "init_command": "SET foreign_key_checks = 0;",
    },                      # Set to empty string for default.
    }
}
elif socket.gethostname() == 'wf-103-44-220-147.webfaction.com':
    DEBUG = TEMPLATE_DEBUG = False
    ALLOWED_HOSTS = ['*']    
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'naman',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'rt8055',
        'PASSWORD': 'Starthere66%',
        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',
	'OPTIONS': {
         "init_command": "SET foreign_key_checks = 0;",
    },                      # Set to empty string for default.
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_PATH = os.path.join(BASE_DIR,'static')

MEDIA_URL = '/media/'
STATICFILES_DIRS = (
    STATIC_PATH,
)

CSRF_COOKIE_DOMAIN = None

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')

STATICFILES_DIRS = (
    STATIC_PATH,
)

CSRF_COOKIE_DOMAIN = None


PAYU_MERCHANT_KEY = "IZpVrp",

PAYU_MERCHANT_SALT = "uvARXRe4",

# Change the PAYU_MODE to 'LIVE' for production.
PAYU_MODE = "TEST"

EMAIL_HOST = 'smtp.webfaction.com'

EMAIL_HOST_USER = 'rtxingmail'

EMAIL_HOST_PASSWORD = 'Pondicherry66%'

EMAIL_PORT = 587

EMAIL_USE_TLS = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

#DEFAULT_FROM_EMAIL = 'contact@smartvizag.com'

SERVER_EMAIL = 'contact@smartvizag.com'
