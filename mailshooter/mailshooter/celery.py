import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mailshooter.settings')

app = Celery('mailshooter')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'warming_every_10_seconds' : {
        'task' : 'mails.tasks.warming_email',
        'schedule' : 10, # Executes in each 10 seconds
        'args' : ('mfsi.atishays@gmail.com',)
    },

    'goals_reminder_weekdays' : {
        'task' : 'mails.tasks.goals_reminder_email',
        'schedule' : crontab(day_of_week='1,2,3,4,5'), # Executes once in a day excluding(Sat, Sun)
        'args' : ('mfsi.atishays@gmail.com',)
    }
}
app.conf.timezone = 'UTC'