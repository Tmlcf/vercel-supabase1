import os
import sys

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Import WSGI application directly
from myproject.wsgi import application

# Export for Vercel
app = application