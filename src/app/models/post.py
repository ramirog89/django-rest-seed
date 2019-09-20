from __future__ import unicode_literals
from django.db import models

class PostModel(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateField()