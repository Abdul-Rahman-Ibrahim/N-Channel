from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=140)
    age = models.PositiveBigIntegerField(null=True, blank=True)