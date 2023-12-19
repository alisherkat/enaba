"""
WSGI config for enaba project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application
from pathlib import Path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'enaba.settings')

application = get_wsgi_application()


app = application
