import time

from celery import shared_task

@shared_task
def working_task():
    time.sleep(5)
    return True
