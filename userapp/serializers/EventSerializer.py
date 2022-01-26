from rest_framework import serializers
from userapp.models.event import Event

class EventSerializer(serializers.ModelSerializer):
    type_name = serializers.CharField(source='type.type', read_only=True)

    class Meta:
        model = Event
        #fields = '__all__'
        fields = ('internal_id', 'title', 'description', 'date', 'type_name','users')


