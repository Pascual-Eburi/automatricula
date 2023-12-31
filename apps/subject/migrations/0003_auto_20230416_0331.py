# Generated by Django 3.1.7 on 2023-04-16 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modality', '0001_initial'),
        ('phase', '0002_auto_20230415_1253'),
        ('subject', '0002_auto_20230415_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='modality_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subjects', to='modality.modality', verbose_name='Id modalidad'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='phase_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subjects', to='phase.phase', verbose_name='Id fase'),
        ),
    ]
