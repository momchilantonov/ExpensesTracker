# Generated by Django 3.2.4 on 2021-06-23 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='expenses',
        ),
    ]