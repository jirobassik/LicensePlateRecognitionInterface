import django.db
from django.shortcuts import render
from license_plate_table.models import License_plate
from utilities.data_repr.column_func import get_columns, init_dict_requests


def view_data_table(request):
    main_objs = License_plate.objects.all()
    columns = get_columns()
    return render(request, 'license_plate_table/license_plate_table.html',
                  {'license_plate': main_objs, 'columns': columns})


def search_view(request):
    main_objs = License_plate.objects.all()
    columns = get_columns()
    if request.method == 'GET':
        search_request = init_dict_requests(request)
        if string_query := search_request['search_query'].string_search:
            try:
                main_objs = search_request['search_query'].func_search(string_query, main_objs)
                columns = [column for column in main_objs.columns if column != "id"]
            except django.db.utils.ProgrammingError:
                main_objs = License_plate.objects.all()
                columns = get_columns()
        else:
            searched_valid_input = dict(
                filter(lambda text_query: True if text_query[1].string_search else False, search_request.items()))
            for key in searched_valid_input:
                main_objs = searched_valid_input[key].func_search(searched_valid_input[key].string_search, main_objs)
    return render(request, 'license_plate_table/license_plate_table.html',
                  {'license_plate': main_objs, 'columns': columns})
