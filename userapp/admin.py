from django.contrib import admin

from userapp.models.user import User
from userapp.models.event import Event
from userapp.models.event_type import EventType


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)

class EventAdmin(admin.ModelAdmin):
    pass
admin.site.register(Event, EventAdmin)

class EventTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(EventType, EventTypeAdmin)
