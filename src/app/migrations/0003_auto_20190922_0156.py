# Generated by Django 2.2.5 on 2019-09-22 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190922_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='body',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='tagmodel',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
