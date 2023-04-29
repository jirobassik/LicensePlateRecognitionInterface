from django.shortcuts import render
from django.views import generic

from profile_and_site_settings.models import Profile, WhiteList, LicensePlateList
from profile_and_site_settings.forms import ProfileForm


class SettingsView(generic.View):
    profile_form = ProfileForm
    # initial = {"key": "value"}
    template_name = "profile_and_site_settings/settings.html"

    def get(self, request):
        form = self.profile_form()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.profile_form(request.POST)
        if form.is_valid():
            form.save()
        print(form)
        return render(request, self.template_name, {"form": form})
