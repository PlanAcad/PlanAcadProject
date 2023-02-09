from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['https://planacad.azurewebsites.net']
# Application definition


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ssrtmvzt',
        'USER': 'ssrtmvzt',
        'PASSWORD': 'n_c7YjoD3_deM1UAEtVcOp7UW7JotqC4',
        'HOST': 'chunee.db.elephantsql.com',
        'PORT': '',
    },
}  
"""""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'planacad',
    }
}
"""


