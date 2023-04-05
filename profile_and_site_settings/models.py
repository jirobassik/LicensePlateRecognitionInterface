from django.db import models
from django.contrib.auth.models import User

from django_countries.fields import CountryField


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = CountryField()
    city = models.CharField(verbose_name='City', max_length=50)

    def __str__(self):
        return self.user.__str__()