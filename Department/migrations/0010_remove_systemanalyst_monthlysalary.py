# Generated by Django 4.1.2 on 2022-10-10 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Department', '0009_systemanalyst_monthlysalary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='systemanalyst',
            name='MonthlySalary',
        ),
    ]