# Generated by Django 4.1.2 on 2022-10-05 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0002_remove_town_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='town',
            name='is_city',
            field=models.BooleanField(default=False),
        ),
    ]
