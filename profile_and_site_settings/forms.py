from django import forms

from django_countries.fields import CountryField
from django_countries import countries

from profile_and_site_settings.models import Profile, LicensePlateList, WhiteList


class ProfileForm(forms.Form):
    email = forms.EmailField(label="Email")
    username = forms.CharField(label="User name", max_length=30)
    password = forms.PasswordInput()
    confirm_password = forms.PasswordInput()
    first_name = forms.CharField(label="First name", max_length=30)
    last_name = forms.CharField(label="Last name", max_length=30)


class LicensePlateForm(forms.Form):
    pass


class WhiteListForm(forms.Form):
    pass
