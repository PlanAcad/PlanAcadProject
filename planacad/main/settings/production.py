from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n%)qyk7n&3_uk+3zx&!z7ba1bykb1!9!0xhi$dw)n*v7kewn+9'

# SECURITY WARNING: don't run with debug turned on in production!
# Application definition

ALLOWED_HOSTS = ['https://planacad.azurewebsites.net']
DEBUG = False
SCM_DO_BUILD_DURING_DEPLOYMENT=True
WEBSITE_WEBDEPLOY_USE_SCM =True
ENABLE_ORYX_BUILD = True

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
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/




