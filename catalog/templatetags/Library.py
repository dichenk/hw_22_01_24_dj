from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from django.conf import settings


register = template.Library()

@register.filter(needs_autoescape=True)
def lololobebebe(text, autoescape=True):
    result = settings.MEDIA_URL + str(text)
    return mark_safe(result)

@register.simple_tag
def dzhaga_dzhaga(text):
    return mark_safe(settings.MEDIA_URL + str(text))
