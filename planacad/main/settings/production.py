from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
# Application definition


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n%)qyk7n&3_uk+3zx&!z7ba1bykb1!9!0xhi$dw)n*v7kewn+9'

SCM_DO_BUILD_DURING_DEPLOYMENT=True

DEBUG = False

ALLOWED_HOSTS = ['https://planacad.azurewebsites.net']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    "whitenoise.runserver_nostatic", # To ease serving static files via Azure 
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'planificaciones'
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "planificaciones/templates")],
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

WSGI_APPLICATION = 'main.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'es-ES'

TIME_ZONE = 'America/Buenos_Aires'

DATE_FORMAT = 'd/m/Y'

DATE_INPUT_FORMATS = ['%d/%m/%Y']

USE_I18N = True

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = os.environ.get("DJANGO_STATIC_URL", "/static/")  
STATIC_ROOT = os.environ.get("DJANGO_STATIC_ROOT", "./static/")  
STATICFILES_STORAGE = ('whitenoise.storage.CompressedManifestStaticFilesStorage') 

LOGIN_REDIRECT_URL = '/asignaturas/'
LOGOUT_REDIRECT_URL = '/accounts/login/'


