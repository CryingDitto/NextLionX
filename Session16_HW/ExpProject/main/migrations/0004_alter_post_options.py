# Generated by Django 4.0.4 on 2022-08-03 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_delete_register'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-updated_dt', 'author'), 'verbose_name': 'post', 'verbose_name_plural': 'posts'},
        ),
    ]
