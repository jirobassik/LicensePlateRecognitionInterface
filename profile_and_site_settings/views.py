from django.shortcuts import render
from django.views import generic

from profile_and_site_settings.models import Profile


class SettingsListView(generic.ListView):
    model = Profile
    template_name = 'settings.html'
