# Generated by Django 4.0.3 on 2022-05-16 01:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0002_alter_post_event_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='numviews',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='event_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]