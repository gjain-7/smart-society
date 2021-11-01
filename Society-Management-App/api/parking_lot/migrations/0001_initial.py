# Generated by Django 3.2.7 on 2021-10-23 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gate_Log',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('entry_time', models.DateTimeField(editable=False, verbose_name='Entry Time')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('exited', models.BooleanField(default=True, verbose_name='Has Exited')),
                ('exit_time', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Exit Time')),
                ('vehicle_type', models.CharField(blank=True, max_length=25, null=True, verbose_name='Vehicle Type')),
                ('vehicle_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Vehicle Number')),
            ],
            options={
                'verbose_name': 'Gate Entry',
                'verbose_name_plural': 'Gate Log',
                'ordering': ['-entry_time'],
            },
        ),
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('parking_id', models.CharField(max_length=25, primary_key=True, serialize=False, verbose_name='Parking ID')),
                ('filled', models.BooleanField(blank=True, editable=False, null=True)),
            ],
            options={
                'verbose_name': 'Parking',
                'verbose_name_plural': 'Parking Spaces',
                'ordering': ['parking_id'],
            },
        ),
    ]
