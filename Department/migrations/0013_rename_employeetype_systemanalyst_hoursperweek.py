# Generated by Django 4.1.2 on 2022-10-10 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Department', '0012_remove_systemanalyst_hoursperweek_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='systemanalyst',
            old_name='EmployeeType',
            new_name='HoursPerWeek',
        ),
    ]