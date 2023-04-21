from django.shortcuts import render
from django.views import generic

from profile_and_site_settings.models import Profile, WhiteList, LicensePlateList
from profile_and_site_settings.forms import ProfileForm


class SettingsListView(generic.View):

    def get(self, request):
        form = ProfileForm()
        template_name = "profile_and_site_settings/settings.html"
        return render(request, template_name, {"form": form})

    def post(self, request):
        form = ProfileForm()
        template_name = "profile_and_site_settings/settings.html"
        return render(request, template_name, {"form": form})
