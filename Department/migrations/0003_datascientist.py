# Generated by Django 4.1.2 on 2022-10-07 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Department', '0002_softwaretester'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataScientist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('EmployeeID', models.IntegerField()),
                ('HoursPerWeek', models.IntegerField()),
                ('MonthlySalary', models.IntegerField()),
            ],
        ),
    ]
