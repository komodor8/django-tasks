# Generated by Django 2.2.7 on 2019-11-21 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20191121_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='task',
            field=models.ForeignKey(default=21, on_delete=django.db.models.deletion.CASCADE, to='tasks.Task'),
            preserve_default=False,
        ),
    ]
