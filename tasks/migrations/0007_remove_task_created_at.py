# Generated by Django 2.2.7 on 2019-12-09 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20191209_1304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='created_at',
        ),
    ]
