from django import template

register = template.Library()


# Создание тега
@register.simple_tag
def media_path(data):
    return '/media/' + str(data)


# Создание фильтра
@register.filter
def media_path(value):
    return '/media/' + str(value)
