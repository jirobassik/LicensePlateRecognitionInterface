from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User
from django_countries.fields import CountryField


class License_plate(models.Model):
    license_plate = models.CharField("License plate", max_length=40, null=True)
    region = models.CharField("Region", max_length=20, null=True, blank=True)
    date_time = models.DateTimeField("Date and time", null=False)
    user_name = models.CharField("User name", max_length=50, null=False)
    field_name = models.ImageField("Image", upload_to=None, height_field=None, width_field=None, max_length=100)
    source = models.CharField("Source", max_length=30, null=False)

    def __str__(self):
        return self.license_plate

    @staticmethod
    def get_absolute_url():
        return reverse('license_plate_data')


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = CountryField()
    city = models.CharField(verbose_name='City', max_length=50)

    def __str__(self):
        return self.user.__str__()
