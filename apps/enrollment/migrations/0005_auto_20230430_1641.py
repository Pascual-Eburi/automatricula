# Generated by Django 3.1.7 on 2023-04-30 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enrollment', '0004_auto_20230429_1939'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enrollment',
            old_name='enroment_data',
            new_name='enrollment_date',
        ),
    ]