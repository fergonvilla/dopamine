"""Production settings and globals."""
from __future__ import absolute_import
from os import environ

from django.core.exceptions import ImproperlyConfigured

from settings.base import *


def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)


DEBUG = False
TEMPLATE_DEBUG = DEBUG

SITE_URL = "http://somesite.com"

ALLOWED_HOSTS = ['www.somesite.com', ]

SECRET_KEY = get_env_setting("DOPAMINE_KEY")

EMAIL_SENDER = 'Info<info@fake-email.com>'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_PORT = environ.get('EMAIL_PORT', 587)
EMAIL_HOST = environ.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', 'info@fake-email.com')
EMAIL_HOST_PASSWORD = get_env_setting('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True

# EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# # See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
# CACHES = {}

# Use postgre in produciton
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dopamine_db',
        'USER': 'admin',
        'PASSWORD': get_env_setting('DB_ADMIN_PASS'),
        'HOST': 'localhost',
        'PORT': '',
    }
}

INTERNAL_IPS = ('127.0.0.1',)

# https://docs.djangoproject.com/en/1.6/topics/http/sessions/#module-django.contrib.sessions
# SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'


INSTALLED_APPS += (
    # 'raven.contrib.django.raven_compat',
)
