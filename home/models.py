from django.db import models
from datetime import datetime



class Guest(models.Model):
    num = models.CharField(max_length=6)
    entry = models.DateTimeField(default=datetime.now())
    exit = models.DateTimeField(default=datetime.now())
    flag =  models.IntegerField(default=1)
    def __str__(self):
        return self.num


class Registered(models.Model):
    num = models.CharField(max_length=6)

    def __str__(self):
        return self.num



