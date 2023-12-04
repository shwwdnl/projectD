from django import template

from config.settings import MEDIA_URL

register = template.Library()


@register.simple_tag
def media_tag(product):
    return MEDIA_URL + str(product)