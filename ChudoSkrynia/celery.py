import os
from celery import Celery
from django.conf import settings
# Основыне настройки Django для celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChudoSkrynia.settings')
app = Celery('ChudoSkrynia')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)