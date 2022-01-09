from django.urls import path
from apiapp.api import event
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('api/v1/events/', event.events, name='events'),
]