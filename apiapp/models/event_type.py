from django.db import models

class EventType(models.Model):
    internal_id = models.AutoField(primary_key = True)
    type = models.CharField(max_length=255)

    def __str__(self):
            return f"{self.type}"

    class Meta:
            db_table = "event_type"