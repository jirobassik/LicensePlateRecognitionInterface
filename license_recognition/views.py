from django.shortcuts import render

def view_license_recognition(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        # Сохраняем файл на сервере, например, в директории media
        with open(f'media/{image.name}', 'wb+') as destination:
            for chunk in image.chunks():
                destination.write(chunk)

    return render(request, 'license_recognition/license_recignition.html')
