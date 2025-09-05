#!/usr/bin/env python

import os
import sys
from pathlib import Path

# Add project root to Python path
BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Configure Django
import django
from django.conf import settings
from django.core.wsgi import get_wsgi_application

# Initialize Django
django.setup()

# Create WSGI application
application = get_wsgi_application()

# For Vercel
def app(environ, start_response):
    return application(environ, start_response)

# Alternative export
handler = application