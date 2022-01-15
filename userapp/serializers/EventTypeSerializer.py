from rest_framework import serializers
from userapp.models.event_type import EventType

class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = '__all__'