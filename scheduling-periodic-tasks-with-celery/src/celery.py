import os
from celery import Celery
import random, string

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')
app = Celery('src')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'add-every-5-seconds': {
            'task': 'tasks.tasks.add_user_timestamp',
            'schedule': 5,
    }
}

