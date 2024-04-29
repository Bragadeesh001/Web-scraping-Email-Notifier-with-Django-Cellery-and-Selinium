import os
from celery import Celery
# from celery.schedules import crontab
from cfehome import settings as app_setting

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cfehome.settings')

app = Celery('cfehome', broker = app_setting.CELERY_BROKER_URL)

# Using a string means that  worker  dont have to serialize
# the configuration  object to  child processes
# -namespace='CELERY' mean all celery related configuration keys should have  a 'CELERY_' prefix

app.config_from_object('django.conf:settings', namespace='CELERY')

#Load task modules from all  registered django app configs
app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     'add every 30 seconds':{
#         'task': 'movies.tasks.add',
#         'schedule': 30.0,
#         'args': (20,10),
#     }
# }

# To run
# celery -A cfehome worker --beat

# this command shows all the task info 
# celery -A cfehome worker --beat -l INFO

