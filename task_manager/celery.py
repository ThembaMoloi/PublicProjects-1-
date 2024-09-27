from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings')

app = Celery('task_manager')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# Namespace='CELERY' means all celery-related configuration keys
# should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

# Celery Beat Schedule
app.conf.beat_schedule = {
    'send-reminders-every-hour': {
        'task': 'tasks.tasks.send_reminder_notifications',
        'schedule': crontab(minute=0, hour='*'),  # Every hour at minute 0
    },
    'create-recurring-tasks-daily': {
        'task': 'tasks.tasks.create_recurring_tasks',
        'schedule': crontab(minute=0, hour=0),  # Every day at midnight
    },
}