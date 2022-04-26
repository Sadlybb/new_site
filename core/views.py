from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic.list import ListView

from .models import Brand, Color, DeviceModel, Device
# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'core/registration/login.html'

    succes_url = 'admin'


class BrandListView(ListView):
    model = Brand
    template_name = 'core/devices/brand_list.html'
    context_object_name = 'brands'


class ColorListView(ListView):
    model = Color
    template_name = 'core/devices/color_list.html'
    context_object_name = 'colors'


class DeviceModelListView(ListView):
    model = DeviceModel
    template_name = 'core/devices/device_model_list.html'
    context_object_name = 'device_models'


class DeviceListView(ListView):
    model = Device
    template_name = 'core/devices/device_list.html'
    context_object_name = 'devices'
