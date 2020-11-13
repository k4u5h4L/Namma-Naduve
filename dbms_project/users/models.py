from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    #first_name = models.CharField(max_length=50)
    #last_name = models.CharField(max_length=50)

    #user_name = models.CharField(max_length=50)

    #email = models.CharField(max_length=60)
    pass
    # add additional fields in here

    def __str__(self):
        return self.username
