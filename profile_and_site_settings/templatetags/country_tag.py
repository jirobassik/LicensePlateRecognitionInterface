from django import template
from django_countries import countries

register = template.Library()


@register.simple_tag
def country_tag():
    country_choice = ((tag, name) for tag, name in list(countries)[:3])
    return country_choice
