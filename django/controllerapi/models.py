from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class Device(models.Model):

    serial = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # def __str__(self):
    #        return self.serial


class Task(models.Model):

    # using enumeration for frequency field

    class Frequency(models.TextChoices):
        HOURLY = "hourly", "Hourly"
        WEEKLY = "weekly", "Weekly"
        MONTHLY = "monthly", "Monthly"
        YEARLY = "yearly", "Yearly"

    class Type(models.TextChoices):
        ONETIME = "onetime", "OneTime"
        RECURRENT = "recurrent", "Recurrent"

    name = models.CharField(max_length=100, blank=True)
    _type = models.CharField(max_length=100, blank=True, choices=Type.choices)
    active = models.BooleanField(default=True, blank=True, null=True)
    frequency = models.CharField(max_length=50, choices=Frequency.choices, blank=True)
    executed = models.BooleanField(default=False)
    recurrence_id = models.IntegerField(default=0)
    recurrence_rule = models.CharField(max_length=500, blank=True)
    recurrence_exceptions = models.CharField(max_length=500, blank=True)
    device = models.ForeignKey(Device, on_delete=models.SET_NULL, null=True)

    # def get_absolute_url(self):
    #     return reverse("taskdetail", args=[str(self.pk)])

    # def get_tasks_info(self):
    #     return self.name + " type is " + self._type

    # def __str__(self):
    #     return f"{self.name}, {self._type},{self.active},{self.frequency},{self.device}"


class Sensor(models.Model):
    class Sensor_Name(models.TextChoices):
        SOIL_MOISTURE = "soil_moisture", "Soil_Moisture"
        TEMPERATURE = "temperature", "Temperature"
        HUMIDITY = "humidity", "Humidity"
    sensor_id = models.CharField(max_length=200, default=0)
    name = models.CharField(max_length=50, choices=Sensor_Name.choices)


class Data(models.Model):

    datetime = models.DateTimeField( null=True, blank=True )
    value = models.FloatField(blank=True, null=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.SET_NULL, null=True)
    device = models.ForeignKey(Device, on_delete=models.SET_NULL, null=True)
