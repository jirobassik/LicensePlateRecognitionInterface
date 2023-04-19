from django.shortcuts import render
from django.views import generic

from profile_and_site_settings.models import Profile, WhiteList, LicensePlates


class SettingsListView(generic.ListView):
    model = Profile
    template_name = 'profile_and_site_settings/settings.html'
