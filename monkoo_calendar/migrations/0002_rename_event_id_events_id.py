# Generated by Django 4.0.2 on 2022-05-12 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monkoo_calendar', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='event_id',
            new_name='id',
        ),
    ]
