# Generated by Django 2.2.5 on 2019-09-22 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AlterModelOptions(
            name='postmodel',
            options={'ordering': ('title',)},
        ),
        migrations.AddField(
            model_name='postmodel',
            name='slug',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='tags',
            field=models.ManyToManyField(to='app.TagModel'),
        ),
    ]