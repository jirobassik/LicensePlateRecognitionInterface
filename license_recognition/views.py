import mimetypes
import os

from django.http import HttpResponse
from django.shortcuts import render
from license_plate_table.models import License_plate
from datetime import datetime
from django.core.files.uploadedfile import SimpleUploadedFile
from profile_and_site_settings.models import WhiteList
import json


def view_license_recognition(request):
    if 'upload_photo' in request.POST:
        if image := request.FILES.get('image', False):
            save_photo('license_recognition/static/image', image)
            recognition_result = number_finder(f'license_recognition/static/image/{image.name}')
            new_license_plate = License_plate()
            new_license_plate.license_plate = recognition_result
            new_license_plate.region = 'BY'
            new_license_plate.date_time = datetime.now()
            new_license_plate.user_name = '-'
            new_license_plate.source = 'image'
            image_data = open(f"license_recognition/static/image/{image.name}", "rb").read()
            new_license_plate.field_name = SimpleUploadedFile(name=f"{image.name}", content=image_data, )
            new_license_plate.save()
            return render(request, 'license_recognition/license_recignition.html',
                          {'rec_res': recognition_result,
                           'path_to_file': f'/static/image/{image.name}'})
    if 'add_owner' in request.POST:
        lic_plate = request.POST.get('lic_plate', 'unknown')
        region = request.POST.get('region', 'BY')
        owner = request.POST.get('owner', 'unknown')
        white_list = WhiteList()
        white_list.license_plate = lic_plate
        white_list.user_name = owner
        white_list.save()
    if 'save' in request.POST:
        lic_plate = request.POST.get('lic_plate', 'unknown')
        region = request.POST.get('region', 'BY')
        owner = request.POST.get('owner', 'unknown')
        # load_json(lic_plate, region, owner)
        json_save_one(lic_plate, region, owner)
        # Открываем файл JSON на запись
        return download_file()

    return render(request, 'license_recognition/license_recignition.html')


def number_finder(path_to_file: str):
    return '1111'


def save_photo(path_to_folder: str, image):
    with open(f'{path_to_folder}/{image.name}', 'wb+') as destination:
        for chunk in image.chunks():
            destination.write(chunk)


def download_file():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'res_rec.json'
    filepath = BASE_DIR + '/license_recognition/static/json/' + filename
    path = open(filepath, 'r', encoding="utf-8",)
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response


def json_save_one(lic_plate, region, owner):
    with open('license_recognition/static/json/res_rec.json', encoding='utf-8') as file_json:
        data = json.load(file_json)
    data['lic_plate'] = lic_plate
    data['region'] = region
    data['owner'] = owner
    with open('license_recognition/static/json/res_rec.json', 'w', encoding='utf-8') as file_json:
        json.dump(data, file_json, indent=4, ensure_ascii=False)
