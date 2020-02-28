from django import template

register=template.Library()

@register.filter()
def mydd(num,num2):
    return num+num2