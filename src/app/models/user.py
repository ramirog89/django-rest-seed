from __future__ import unicode_literals
from django.db import models

class UserModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)