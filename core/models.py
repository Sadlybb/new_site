from django.db import models

# Create your models here.


class Brand(models.Model):
    brand = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.brand


class Color(models.Model):
    color = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.color


class DeviceModel(models.Model):
    brand = models.ForeignKey(
        Brand, on_delete=models.PROTECT, related_name='models')
    color = models.ForeignKey(
        Color, on_delete=models.PROTECT, related_name='models')
    device_model = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.device_model} {self.color}"


class Device(models.Model):
    INTERNAL_STORAGE_CHOICES = {
        ("4gb", "4GB"),
        ("8gb", "8GB"),
        ("16gb", "16GB"),
        ("32gb", "32GB"),
        ("64gb", "64GB"),
        ("128gb", "128GB"),
        ("256gb", "256GB"),
        ("512gb", "512GB"),
        ("1tb", "1TB"),
        ("2tb", "2TB"),
    }

    device_models = models.ForeignKey(
        DeviceModel, on_delete=models.PROTECT, related_name='devices')
    serial_number = models.CharField(max_length=50)
    imei_1 = models.CharField(max_length=15)
    internal_storage = models.CharField(
        max_length=5, choices=INTERNAL_STORAGE_CHOICES)

    def __str__(self) -> str:
        return f"{self.device_models}**********{self.imei_1}"
