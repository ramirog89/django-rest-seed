from __future__ import unicode_literals
from django.db import models
import datetime

class AccountModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    created_at = models.DateField(default=datetime.date.today)

    class Meta:
        db_table = 'account'
        ordering = ('name',)
        app_label = 'something'

    def __str__(self):
        return self.name

