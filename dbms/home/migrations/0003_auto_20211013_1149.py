# Generated by Django 3.2.7 on 2021-10-13 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20211005_2251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='society_staff',
            name='img',
        ),
        migrations.AlterField(
            model_name='society_staff',
            name='Aadhar',
            field=models.CharField(max_length=12, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='society_staff',
            name='mobile',
            field=models.CharField(max_length=10),
        ),
    ]