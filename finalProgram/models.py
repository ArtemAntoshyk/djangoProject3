from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    groups = models.ManyToManyField(
        'auth.Group',
        related_name = "custemuser_set",
        blank=True,
        verbose_name='groups',
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups."

    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name="custemuser_set",
        blank=True,
        verbose_name='groups',
        help_text="Specific permissions for this user"
    )

