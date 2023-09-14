# Generated by Django 3.1.7 on 2023-04-16 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geodata', '0003_auto_20230414_1205'),
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamCenter',
            fields=[
                ('center_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nombre')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Dirección')),
                ('district_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='geodata.district', verbose_name='Id distrito')),
            ],
            options={
                'verbose_name': 'Centro de Examen',
                'verbose_name_plural': 'Centros de Examenes',
            },
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('classroom_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='nombre')),
                ('capacity', models.PositiveIntegerField(default=0, verbose_name='Capacidad')),
                ('center_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.examcenter', verbose_name='Id centro')),
            ],
            options={
                'verbose_name': 'Aula',
                'verbose_name_plural': 'Aulas',
            },
        ),
    ]