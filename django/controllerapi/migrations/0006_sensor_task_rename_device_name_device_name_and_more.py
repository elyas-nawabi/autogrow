# Generated by Django 4.0.1 on 2022-06-07 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controllerapi', '0005_command_executed_command_recurrence_exceptions_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('soil_moisture', 'Soil_Moisture'), ('temperature', 'Temperature'), ('humidity', 'Humidity')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('type', models.CharField(blank=True, choices=[('onetime', 'OneTime'), ('recurrent', 'Recurrent')], max_length=100)),
                ('active', models.BooleanField(blank=True, default=True, null=True)),
                ('frequency', models.CharField(blank=True, choices=[('hourly', 'Hourly'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('yearly', 'Yearly')], max_length=50)),
                ('executed', models.BooleanField(default=False)),
                ('recurrence_id', models.IntegerField(default=0)),
                ('recurrence_rule', models.CharField(blank=True, max_length=500)),
                ('recurrence_exceptions', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.RenameField(
            model_name='device',
            old_name='device_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='data',
            name='Data_id',
        ),
        migrations.RemoveField(
            model_name='data',
            name='device_id',
        ),
        migrations.RemoveField(
            model_name='device',
            name='device_id',
        ),
        migrations.AddField(
            model_name='data',
            name='device',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='controllerapi.device'),
        ),
        migrations.AddField(
            model_name='device',
            name='serial',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='data',
            name='value',
            field=models.FloatField(blank=True, max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Command',
        ),
        migrations.AddField(
            model_name='task',
            name='device',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='controllerapi.device'),
        ),
        migrations.AlterField(
            model_name='data',
            name='sensor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='controllerapi.sensor'),
        ),
    ]