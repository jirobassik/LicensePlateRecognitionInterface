from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.sign_in, name='sign_in'),
    path('register/', views.register, name='register'),
]