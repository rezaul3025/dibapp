from django.db import models
from django.conf import settings

from userapp.models.event_type import EventType
from userapp.models.user import User

class Event(models.Model):
    internal_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    date = models.DateTimeField()
    type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    users = models.ManyToManyField(User)

    def __str__(self):
        return f"{self.event.title}, {self.title},{self.description},{self.date.strftime(settings.DATETIME_FORMAT)}"
    class Meta:
        db_table = "event"
