from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from userapp.models.user import User
from userapp.models.event import Event
from userapp.serializers.EventSerializer import EventSerializer

@api_view(['GET'])
def events(request):
    data = {'test':'test','test1':'test1'}
    return Response(data)



class EventDetails(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, userId, format=None):
        user = User.objects.get(email__iexact=userId)
        events = Event.objects.filter(users__in = user)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

