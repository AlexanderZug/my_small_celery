import random
import string

from celery import shared_task

from .models import MyModel


@shared_task
def new_print():
    new_name = ''.join([random.choice(string.ascii_letters) for _ in range(5)])
    new_obj = MyModel.objects.create(name=new_name)
    return new_obj.name
