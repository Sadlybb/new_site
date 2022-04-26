from django.contrib import admin

from .models import Brand, Color, Device, DeviceModel

# Register your models here.


admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(DeviceModel)
admin.site.register(Device)
