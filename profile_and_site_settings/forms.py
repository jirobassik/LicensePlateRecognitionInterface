from django import forms

from profile_and_site_settings.models import Profile, LicensePlateList, WhiteList


class ProfileForm(forms.Form):
    class Meta:
        pass


class LicensePlateForm(forms.Form):
    pass


class WhiteListForm(forms.Form):
    pass
