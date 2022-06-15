from celery import Celery
from datetime import timedelta
from . import exporter

# Celery app instantiated from exporter.py
app = Celery('tasks', broker=exporter.REDIS_DB_CRED)

# Celery beat instantiated from exporter.py
app.conf.beat_schedule = {
 'send-summary-every-15-seconds': {
       'task': 'youtube',
       'schedule': timedelta(seconds=15),
    }
}