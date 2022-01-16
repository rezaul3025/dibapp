import uuid
from django.db import models

from userapp.models.role import Role
from userapp.models.user import User

class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=100, unique=False)
    last_name = models.CharField(max_length=100, unique=False)
    phone_number = models.CharField(max_length=10, unique=False, null=False, blank=False)
    roles = models.ManyToManyField(Role)

    class Meta:
        '''
        to set table name in database
        '''
        db_table = "profile"