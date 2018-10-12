# Generated by Django 2.0.2 on 2018-10-12 16:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('studyobjects', '0002_auto_20181012_1502'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Session',
            new_name='UserSession',
        ),
        migrations.AlterField(
            model_name='task',
            name='eta',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 12, 17, 20, 24, 77970, tzinfo=utc)),
        ),
        migrations.AlterUniqueTogether(
            name='task',
            unique_together={('name', 'assessment', 'student')},
        ),
    ]
