# Generated by Django 3.2.4 on 2022-05-22 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controllerapi', '0003_alter_command_task_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='command',
            name='frequency',
            field=models.CharField(blank=True, choices=[('hourly', 'Hourly'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('yearly', 'Yearly')], max_length=10),
        ),
        migrations.AlterField(
            model_name='command',
            name='task_id',
            field=models.IntegerField(default=0),
        ),
    ]
