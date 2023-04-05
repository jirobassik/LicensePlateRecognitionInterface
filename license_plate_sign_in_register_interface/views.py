from django.shortcuts import render

# Create your views here.

def sign_in(request):
    return render(request, 'license_plate_sign_in_register_interface/signin.html')

def register(request):
    return render(request, 'license_plate_sign_in_register_interface/register.html')
