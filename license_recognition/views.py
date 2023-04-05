from django.shortcuts import render


def view_license_recognition(request):
    return render(request, 'license_recognition/license_recignition.html', )

# Create your views here.
