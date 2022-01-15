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
        (MEMBER, 'student'),
        (GUEST, 'teacher'),
        (ADMIN, 'secretary'),
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()
