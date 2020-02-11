from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello World')


def about(request):
    return HttpResponse('我是about')


def zzz(request):
    return HttpResponse('【环球网综合报道】日本共同网10日最新消息称，据日本政府相关人士透露，由于新确认60名以上新型冠状病毒感染者，目前，日本国内的感染者已超过150人')
