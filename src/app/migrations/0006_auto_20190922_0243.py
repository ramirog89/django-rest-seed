# Generated by Django 2.2.5 on 2019-09-22 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_postmodel_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='tags',
        ),
        migrations.AddField(
            model_name='tagmodel',
            name='post',
            field=models.ManyToManyField(to='app.PostModel'),
        ),
    ]
