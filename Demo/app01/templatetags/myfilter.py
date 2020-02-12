from django import template



register=template.Library()

@register.filter()
def myadd(num):
    return num+num
@register.filter()
def cdd(num):
    return num*num
