from celery import shared_task

@shared_task
def add(x,y):
    return x+y

# for using models
# from django.app import apps
# mymodel = apps.get_model('movies','model-name')