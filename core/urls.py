from django.urls import path

from .views import ColorListView, CustomLoginView, BrandListView, DeviceListView, DeviceModelListView, dashboard, customer


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('brand/', BrandListView.as_view(), name='brand_list'),
    path('color/', ColorListView.as_view(), name='color_list'),
    path('device-model/', DeviceModelListView.as_view(), name='device_model_list'),
    path('device/', DeviceListView.as_view(), name='device_list'),
    path('dashboard/', dashboard, name='dashboard'),
    path('customer/', customer, name='customer'),

]
