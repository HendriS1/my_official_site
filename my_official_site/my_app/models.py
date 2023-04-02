from django.db import models


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=120)
    event_date = models.DateTimeField()
    venue = models.CharField(max_length=120)
    manager = models.CharField(max_length=120)
    description = models.CharField(max_length=200, blank=True)


def __str__(self):
    return self.name
