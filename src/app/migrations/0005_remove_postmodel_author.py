# Generated by Django 2.2.5 on 2019-09-22 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_postmodel_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='author',
        ),
    ]
