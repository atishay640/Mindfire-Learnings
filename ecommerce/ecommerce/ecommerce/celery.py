import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')

app = Celery('ecommerce')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'sync-sf-products-to-db-each-5-minutes': {
        'task': 'apps.shop.tasks.sync_products_from_salesforce',
        'schedule': 60*5, 
    },
    'sync-db-orders-to-sf-each-5-minutes': {
        'task': 'apps.shop.tasks.sync_orders_to_saleforce',
        'schedule': 60*5, 
    },
}