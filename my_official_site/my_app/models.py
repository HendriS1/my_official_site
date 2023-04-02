from django.db import models


# Create your models here.
class Event(models.Model):
    """
    This is a database-driven component that stores a single
    Event entry. Each attribute represents a database field.
    """
    name = models.CharField(max_length=120)
    event_date = models.DateTimeField()
    venue = models.CharField(max_length=120)
    manager = models.CharField(max_length=120)
    description = models.CharField(max_length=200, blank=True)


def __str__(self):
    """
    Method that allows us to convert an object to a string
    representation.

    :param self:

    :return: String representation of the object Event.
    """
    return self.name
