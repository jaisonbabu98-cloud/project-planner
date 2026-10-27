from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class RoleChoices(models.TextChoices):
    DEVELOPER = 'Developer','Developer'
    ADMIN = 'Admin','Admin'
    PROJECT_COORDINATOR = 'Project coordinator','Project coordinator'



class profile (AbstractUser):
    role = models.CharField(max_length=20,choices=RoleChoices.choices)

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'

    def __str__(self):
        return self.username