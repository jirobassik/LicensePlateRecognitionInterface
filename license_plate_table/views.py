from django.shortcuts import render
from django.db.models import Q
from license_plate_table.models import License_plate
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline

from utilities.api_ai_query.ai_query import ai_query


def view_data_table(request):
    main_objs = License_plate.objects.all()
    columns = [column.name for column in License_plate._meta.get_fields()
               if column.name != 'id' and column.name != 'field_name']
    return render(request, 'license_plate_table/license_plate_table.html',
                  {'license_plate': main_objs, 'columns': columns})


def search_view(request):
    main_objs = License_plate.objects.all()
    if request.method == 'POST':
        searched = request.POST['query_search']
        print(searched)
        main_objs = License_plate.objects.raw(ai_query(searched))
        columns = [column for column in main_objs.columns if column != "id" and column != 'field_name']
        print(columns)
    return render(request, 'license_plate_table/license_plate_table.html',
                  {'license_plate': main_objs, 'columns': columns})
