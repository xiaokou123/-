from django import template

register=template.Library()

@register.filter()
def mydd(num,num2):
    print(type(num))
    print(type(num2))
    return num+num2
@register.filter()
def tow(num):
    return "%.2f"%num