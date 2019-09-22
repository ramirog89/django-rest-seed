from __future__ import unicode_literals
from django.db import models
from src.app.models.tag import TagModel

class PostModel(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=150, default="")
    body = models.TextField(blank=True)
    date = models.DateField()
    tags = models.ManyToManyField(TagModel)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title