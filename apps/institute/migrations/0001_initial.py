# Generated by Django 3.1.7 on 2023-04-13 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('geodata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('address', models.CharField(max_length=150)),
                ('district_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='geodata.district')),
            ],
            options={
                'verbose_name': 'Institute',
                'verbose_name_plural': 'Institutes',
            },
        ),
    ]
