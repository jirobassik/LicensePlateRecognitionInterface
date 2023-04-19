from django.db import models
from django.contrib.auth.models import User

from django_countries.fields import CountryField


class LicensePlate(models.Model):
    car_model = models.CharField(verbose_name="Model", max_length=100)
    license_plate = models.CharField(verbose_name="License plate", max_length=10)
    region = CountryField(verbose_name="Region")

    def __str__(self):
        return self.license_plate

    class Meta:
        verbose_name = "License plate"
        verbose_name_plural = "License plates"


class WhiteList(models.Model):
    user_name = models.CharField(verbose_name="User name", max_length=100)
    license_plate = models.CharField(verbose_name="License plate", max_length=10)

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = "License plate"
        verbose_name_plural = "License plates"


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = CountryField()
    city = models.CharField(verbose_name="City", max_length=50)
    user_white_list = models.ManyToManyField(WhiteList, verbose_name="User \"White list\"")
    user_license_plate = models.ManyToManyField(LicensePlate, verbose_name="User license plate")
    notifications_about_new_features = models.BooleanField(
        verbose_name="Notification about new features", default=True
    )
    notifications_when_my_license_plate_on_photo = models.BooleanField(
        verbose_name="Notification when my license plate on photo", default=True
    )
    notifications_when_license_from_white_list_on_photo = models.BooleanField(
        verbose_name="Notification when license plate from \"White list\" on photo", default=True
    )
    notifications_when_unfamiliar_license_on_photo = models.BooleanField(
        verbose_name="Notification when unfamiliar license plate on photo", default=True
    )

    def __str__(self):
        return self.user.__str__()

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
