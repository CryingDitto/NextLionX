# Generated by Django 4.0.3 on 2022-05-12 09:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='event_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 12, 9, 39, 26, 536957, tzinfo=utc)),
        ),
    ]
