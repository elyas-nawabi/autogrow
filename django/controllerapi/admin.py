from django.contrib import admin
from .models import Sensor, Task, Data, Device
# Register your models here.

admin.site.register(Task)
admin.site.register(Device)
admin.site.register(Data)
admin.site.register(Sensor)
