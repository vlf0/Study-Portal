from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """ Represent user account containing information about user. """
    user = models.OneToOneField(to=User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    facebook = models.CharField(max_length=50, null=True, blank=True)
    twitter = models.CharField(max_length=50, null=True, blank=True)
    instagram = models.CharField(max_length=50, null=True, blank=True)

