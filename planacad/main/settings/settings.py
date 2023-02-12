import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'n%)qyk7n&3_uk+3zx&!z7ba1bykb1!9!0xhi$dw)n*v7kewn+9'

DEBUG = True

ALLOWED_HOSTS = ['*']

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

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'PlanacadDB',
        'USER': 'sqladmin',
        'PASSWORD': 'CarlosIngeniero2023',
        'HOST': 'planacad-server.database.windows.net',
        'PORT': '1433'
    },
}  

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

LANGUAGE_CODE = 'es-ES'

TIME_ZONE = 'America/Buenos_Aires'

DATE_FORMAT = 'd/m/Y'

DATE_INPUT_FORMATS = ['%d/%m/%Y']

USE_I18N = True

USE_L10N = False

USE_TZ = True

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/staticfiles/'

LOGIN_REDIRECT_URL = '/asignaturas/'
LOGOUT_REDIRECT_URL = '/accounts/login/'

STATICFILES_DIRS = ()

SCM_DO_BUILD_DURING_DEPLOYMENT=True
WEBSITE_WEBDEPLOY_USE_SCM =True 
ENABLE_ORYX_BUILD = True