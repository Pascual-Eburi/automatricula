# Generated by Django 3.1.7 on 2023-05-07 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20230430_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='rol',
            field=models.CharField(choices=[('student', 'STUDENT'), ('institute_staff', 'INSTITUTE_STAFF'), ('staff', 'STAFF'), ('admin_staff', 'ADMIN_STAFF')], default='student', max_length=30),
        ),
    ]
