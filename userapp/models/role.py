import uuid
from django.db import models


class Role(models.Model):
    '''
    The Role entries are managed by the system,
    automatically created via a Django data migration.
    '''
    MEMBER = 1
    GUEST = 2
    ADMIN = 3
    ROLE_CHOICES = (
        (MEMBER, 'member'),
        (GUEST, 'guest'),
        (ADMIN, 'admin'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    name = models.IntegerField(choices=ROLE_CHOICES, editable=True, default=1)

    def __str__(self):
        return self.name

    class Meta:
        '''
        to set table name in database
        '''
        db_table = "role"
