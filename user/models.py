import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=300)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.BigIntegerField()
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(datetime.datetime.now())

    class Meta:
        db_table = 'user'
