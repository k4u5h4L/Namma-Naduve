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

    # The extra fields we need to add to the custom user model

    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # location = models.CharField(max_length=100, null=True)
    # phone_no = models.CharField(max_length=14, null=True)
    # personal_site = models.CharField(max_length=60, null=True)
    # bio = models.CharField(max_length=500, null=True)
    # full_name = models.CharField(max_length=50, null=True)

    # image = models.ImageField(default='default.jpg', upload_to='profile_pics')


class Profile(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, null=True, blank=True)
    phone_no = models.CharField(max_length=14, null=True, blank=True)
    personal_site = models.CharField(max_length=60, null=True, blank=True)
    bio = models.CharField(max_length=500, null=True, blank=True)
    full_name = models.CharField(max_length=50, null=True, blank=True)

    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
