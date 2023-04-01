from types import MappingProxyType
from django import template

register = template.Library()


@register.simple_tag
def dynamic_view(column: str, item):
    dict_func = MappingProxyType({'source': item.source,
                                  'region': item.region,
                                  'date_time': item.date_time,
                                  'user_name': item.user_name,
                                  'license_plate': item.license_plate})
    return dict_func[column]
