
import os
import sys
from pathlib import Path

# เพิ่ม project path ให้ Python รู้จัก
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

# ตั้งค่า Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Import Django หลังจากตั้งค่าแล้ว
import django
django.setup()

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# สำหรับ Vercel
app = application