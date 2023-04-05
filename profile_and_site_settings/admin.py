from django.contrib import admin

from profile_and_site_settings.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
