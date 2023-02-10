"""
WSGI config for planacad project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

# from dj_static import Cling

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings.settings')

try:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
except ImportError as exc:
    raise ImportError(
        "Couldn't import Django. Are you sure it's installed and "
        "available on your PYTHONPATH environment variable? Did you "
        "forget to activate a virtual environment?"
    ) from exc
# application = Cling(get_wsgi_application())
