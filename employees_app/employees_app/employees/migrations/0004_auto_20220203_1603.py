# Generated by Django 3.2.11 on 2022-02-03 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_alter_employee_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
