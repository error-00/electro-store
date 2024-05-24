from django import template

register = template.Library()


@register.filter(name="add_spaces")
def add_spaces(value):
    return "{:,.0f}".format(value).replace(",", " ")

