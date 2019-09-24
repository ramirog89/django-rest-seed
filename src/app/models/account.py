from __future__ import unicode_literals
from django.db import models

class AccountModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    created_at = models.DateField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class AccountManager():
    model = AccountModel

    def getAllAccounts():
        return self.model.objects.all()

    def getParticularAccounts():
        return self.model.objects.all()