# Generated by Django 3.2.4 on 2022-05-18 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=200)),
                ('task_name', models.CharField(blank=True, max_length=100)),
                ('task_type', models.CharField(blank=True, max_length=100)),
                ('active', models.BooleanField(blank=True, default=True, null=True)),
                ('frequency', models.CharField(choices=[('hr', 'Hourly'), ('wk', 'Weekly'), ('mn', 'Monthly'), ('yr', 'Yearly')], max_length=10)),
            ],
        ),
    ]
