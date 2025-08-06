"""
ASGI config for strathmore_ict_coding_challenge project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'strathmore_ict_coding_challenge.settings')

application = get_asgi_application()
