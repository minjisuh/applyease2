# events/models.py
from django.db import models

class Calendar(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    calendar = models.ForeignKey(Calendar, related_name='events', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
