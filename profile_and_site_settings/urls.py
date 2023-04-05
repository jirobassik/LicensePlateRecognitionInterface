from django.urls import path

from profile_and_site_settings.views import SettingsListView


urlpatterns = [
    path('', SettingsListView.as_view(), name='profile_settings'),
]
