from django.shortcuts import render
from django.views import generic

from profile_and_site_settings.models import Profile, WhiteList, LicensePlate


class SettingsListView(generic.View):

    def get(self, request):
        template_name = "profile_and_site_settings/settings.html"
        return render(request, template_name)
