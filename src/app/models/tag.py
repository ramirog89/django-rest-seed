from __future__ import unicode_literals
from django.db import models

class TagModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name