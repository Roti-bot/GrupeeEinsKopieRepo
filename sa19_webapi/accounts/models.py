from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserMoreFields(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_link_auth = models.BooleanField()
    phone = models.IntegerField()
    token = models.CharField(max_length=200)
    timestampNow = models.CharField(max_length=200)
    timestampExp = models.CharField(max_length=200)
