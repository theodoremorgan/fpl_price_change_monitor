import os
from celery import Celery
from kombu import Queue, Exchange
import time
import sentry_sdk
from sentry_sdk.integrations.celery import CeleryIntegration

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'price_change_monitor.settings')
app = Celery("price_change_monitor")
app.config_from_object("django.conf:settings", namespace="CELERY")
sentry_dsn = 'https://7615f23ab8bfbb48c068385114746a8b@o4508381635411968.ingest.de.sentry.io/4508381641244752'
sentry_sdk.init(dsn=sentry_dsn, integrations=[CeleryIntegration()])


app.conf.task_queues = [
    Queue('tasks', Exchange('tasks'), routing_key='tasks', queue_arguments={'x-max-priority':10}),
    Queue('dead_letter', routing_key='dead_letter'),
]

app.conf.task_acks_late = True
app.conf.task_default_priority = 5
app.conf.worker_prefetch_multiplier = 1
app.conf.worker_concurrency = 1

base_dir = os.getcwd()
task_folder = os.path.join(base_dir,'price_change_monitor','celery_tasks')

if os.path.exists(task_folder) and os.path.isdir(task_folder):
    task_modules =[]
    for filename in os.listdir(task_folder):
        if filename.endswith('.py'):
            module_name = f'price_change_monitor.celery_tasks.{filename[:-3]}'
            
            module = __import__(module_name, fromlist=['*'])
            
            for name in dir(module):
                obj = getattr(module, name)
                if callable(obj):
                    task_modules.append(f'{module_name}.{name}')

    app.autodiscover_tasks(task_modules)