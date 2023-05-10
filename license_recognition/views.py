from django.shortcuts import render


def view_license_recognition(request):
    if 'upload_photo' in request.POST:
        if image := request.FILES.get('image', False):
            # image = request.FILES.get('image', False)
            print(True)
            print(image)
            # Сохраняем файл на сервере, например, в директории media
            with open(f'static/image/{image.name}', 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)

    return render(request, 'license_recognition/license_recignition.html')
