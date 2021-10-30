# Generated by Django 3.2 on 2021-10-20 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security_gate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gate_log',
            name='vehicle_number',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Vehicle Number'),
        ),
        migrations.AlterField(
            model_name='gate_log',
            name='vehicle_type',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Vehicle type'),
        ),
    ]
