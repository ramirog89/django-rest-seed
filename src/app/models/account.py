from __future__ import unicode_literals
from django.db import models

class AccountModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    created_at = models.DateField()

    class Meta:
        db_table = 'account'
        ordering = ('name',)

    def __str__(self):
        return self.name

class AccountManager:
    model = AccountModel

    def getById(self, pk):
        return self.model.objects.get(pk=pk)

    def getAllAccounts(self):
        return self.model.objects.values()

    def getParticularAccounts(self):
        return self.model.objects.all()