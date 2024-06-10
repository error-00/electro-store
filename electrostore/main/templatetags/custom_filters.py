from django import template
from django.utils.http import urlencode

from main.models import Review

register = template.Library()


@register.filter(name="add_spaces")
def add_spaces(value):
    return "{:,.0f}".format(value).replace(",", " ")


@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context["request"].GET.dict()
    query.update(kwargs)
    return urlencode(query)
