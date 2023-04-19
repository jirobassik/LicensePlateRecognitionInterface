from django.contrib import admin

from profile_and_site_settings.models import Profile, LicensePlates, WhiteList


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(LicensePlates)
class UserLicensePlatesAdmin(admin.ModelAdmin):
    pass


@admin.register(WhiteList)
class UserWhiteListAdmin(admin.ModelAdmin):
    pass
