# -*- coding: utf-8 -*-
"Local isolated configuration"
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


TESTING = LOG_EMAIL = True
DEBUG = True

TIME_ZONE = 'Europe/Madrid'
INTERNAL_IPS = ('127.0.0.1',)


# EMAIL_SENDER = 'Info<info@fake-email.com>'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# EMAIL_PORT = environ.get('EMAIL_PORT', 587)
# EMAIL_HOST = environ.get('EMAIL_HOST', 'smtp.gmail.com')
# EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', 'info@fake-email.com')
# EMAIL_HOST_PASSWORD = get_env_setting('EMAIL_HOST_PASSWORD')
# EMAIL_USE_TLS = True


# Make these unique, and don't share it with anybody.
SECRET_KEY = get_env_setting("DOPAMINE_KEY")

NEVERCACHE_KEY = "89a5b253-c60b-4fcb-8e22-102fa5e09de60cadb181-a078-40d4-be4f-\
                 f61abb1ef863199d04f6-753c-48f7-9c02-ed97a5b785a8"

DATABASES = {
    'default': {
        "ENGINE": 'django.db.backends.sqlite3',
        "NAME": os.path.join(PROJECT_ROOT, "db.sqlite3"),
    }
}

#############
# DYNAMIC SETTINGS #
####################

# set_dynamic_settings() will rewrite globals based on what has been
# defined so far, in order to provide some better defaults where
# applicable. We also allow this settings module to be imported
# without Mezzanine installed, as the case may be when using the
# fabfile, where setting the dynamic settings below isn't strictly
# required.
try:
    from mezzanine.utils.conf import set_dynamic_settings
except ImportError:
    pass
else:
    set_dynamic_settings(globals())
