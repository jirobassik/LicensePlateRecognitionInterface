from django.shortcuts import render
from django.views import generic

from profile_and_site_settings.models import Profile, WhiteList, LicensePlateList
from profile_and_site_settings.forms import ProfileForm
from .models import LicensePlateList

class SettingsView(generic.View):
    profile_form = ProfileForm
    template_name = "profile_and_site_settings/settings.html"

    def get(self, request):
        form = self.profile_form()
        plate_list_data = LicensePlateList.objects.all()
        return render(request, self.template_name, {"form": form, "plate_list": plate_list_data})

    def post(self, request):
        form = self.profile_form(request.POST)
        if form.is_valid():
            form.save()
        if 'add_license_plate' in request.POST:
            # print(True)
            model = request.POST['model']
            license_plate = request.POST['license_plate']
        if 'white_list' in request.POST:
            print(True)
        plate_list_data = LicensePlateList.objects.all()
        return render(request, self.template_name, {"form": form, "plate_list": plate_list_data})
