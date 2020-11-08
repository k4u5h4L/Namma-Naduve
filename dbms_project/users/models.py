from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser

# Create your models here.


# class CustomUser(AbstractUser):
#     # username = models.CharField(max_length=50)

#     T_OR_S = (
#         ('Teacher', 'teacher'),
#         ('Student', 'student')
#     )

#     email = models.CharField(max_length=60)
#     t_s = forms.ChoiceField(choices=T_OR_S, widget=forms.RadioSelect())
#     bio = models.CharField(max_length=100)
#     # add additional fields in here

#     # def __str__(self):
#     #     return self.username
