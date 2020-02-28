from django.shortcuts import render
from django.shortcuts import render_to_response,render
from django.http.response import HttpResponse
import hashlib
from django.http import JsonResponse
# Create your views here.

def index(request):
    return render_to_response('index.html')

def about(request):
    return render_to_response("about.html")
def gbook(request):
    return render_to_response('gbook.html')
def info(request):
    return render_to_response('info.html')
def list(request):
    return render_to_response('list.html')



def Setpassword(password):
    md5=hashlib.md5()
    md5.update(password.encode())
    return md5.hexdigest()

from .forms import *
def Ll(request):
    user=User()
    if request.method=='POST':
        data=User(request.POST)
        if data.is_valid():
            username=data.cleaned_data.get('username')
            password=data.cleaned_data.get('password')
            print(username)
            print(password)
            massage='注册成功'
        else:
            massage=data.errors
    return render(request,'lianxi.html',locals())


def lianxi(request):

    return render(request,'lianxi.html')
def lianxi1(request):
    result={'code':1000,'mag':''}
    username=request.GET.get('username')
    if username:
        result = {'code': 1000, 'mag': '可以注册'}
    else:
        result = {'code': 1001, 'mag': '账户不能为空'}
    return JsonResponse(result)

def lianxi2(request):
    result = {'code': 1000, 'mag': ''}
    username=request.POST.get('username')
    password=request.POST.get('password')
    if username and password:
        result = {'code': 1000, 'mag': '注册成功'}
    else:
        result = {'code': 1001, 'mag': '用户名或密码不能为空'}
    return JsonResponse(result)