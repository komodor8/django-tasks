from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = Celery('mysite')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


@app.task
def add(x, y):
    return x + y


@app.task
def error():
    raise ValueError('oops!')
    pass


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)

'''
launch Celery
celery worker -A mysite -l info -E --concurrency=1000


Launch the server and open the dashboard http://localhost:5555
flower --port=5555

Accessing custom django-admin commands
python manage.py shell

Interpretor
from mysite import celery
res = celery.add.delay(1,2)

res = celery.error.delay()
'''
