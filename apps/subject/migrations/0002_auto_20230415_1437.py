# Generated by Django 3.1.7 on 2023-04-15 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modality', '0001_initial'),
        ('subject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='modality_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='modality.modality', verbose_name='Id modalidad'),
        ),
    ]
