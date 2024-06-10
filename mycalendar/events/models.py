# events/models.py
from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField()

class Calendar(models.Model):
    name = models.CharField(max_length=255)
