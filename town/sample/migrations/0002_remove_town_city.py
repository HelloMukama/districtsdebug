# Generated by Django 4.1.2 on 2022-10-05 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='town',
            name='city',
        ),
    ]
