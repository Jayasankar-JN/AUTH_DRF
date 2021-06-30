from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(blank=True,max_length=255)

    def __str__(self):
        return self.email