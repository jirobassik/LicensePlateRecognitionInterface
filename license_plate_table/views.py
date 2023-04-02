from django.shortcuts import render
from django.db.models import Q
from license_plate_table.models import License_plate
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline

from utilities.api_ai_query.ai_query import ai_query
from types import MappingProxyType


def get_columns():
    return License_plate._meta.get_fields()


def view_data_table(request):
    main_objs = License_plate.objects.all()
    columns = [column.name for column in get_columns()
               if column.name != 'id' and column.name != 'field_name']
    return render(request, 'license_plate_table/license_plate_table.html',
                  {'license_plate': main_objs, 'columns': columns})


def search_view(request):
    main_objs = License_plate.objects.all()
    columns = [column.name for column in get_columns()
               if column.name != 'id' and column.name != 'field_name']
    if request.method == 'GET':
        dict_search_inputs = MappingProxyType(
            {'search_query': (request.GET.get('query_search', None),
                              lambda search, objs: objs.raw(ai_query(search))),
             'search_license_name': (request.GET.get('search_license_name', None),
                                     lambda search, objs: objs.filter(license_plate=search),),
             'selected_region': (request.GET.get('select_region', None),
                                 lambda search, objs: objs.filter(region=search),),
             'start_date': (request.GET.get('start_date', None),
                            lambda search, objs: objs.filter(date_time=search),),
             # 'end_date': request.GET.get('end_date', None),  # Добавить в таблицу
             'user_name': (request.GET.get('user_name', None),
                           lambda search, objs: objs.filter(user_name=search),),
             'select_source': (request.GET.get('select_source', None),
                               lambda search, objs: objs.filter(source=search),)
             })
        if dict_search_inputs['search_query'][0]:
            main_objs = dict_search_inputs['search_query'][1](dict_search_inputs['search_query'][0], main_objs)
            columns = [column for column in main_objs.columns if column != "id" and column != 'field_name']
        else:
            searched_valid_input = dict(filter(lambda x: True if x[1][0] else False, dict_search_inputs.items()))
            for key in searched_valid_input:
                main_objs = searched_valid_input[key][1](searched_valid_input[key][0], main_objs)
    return render(request, 'license_plate_table/license_plate_table.html',
                  {'license_plate': main_objs, 'columns': columns})
