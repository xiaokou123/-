from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator
import hashlib
from django.http import JsonResponse
from .forms import *


# Create your views here.
def index(request):
    article_obj = Article.objects.all().order_by('-date')[:6]
    article_obj1 = Article.objects.filter(recom=1)[:7]
    article_obj2 = Article.objects.all().order_by('-click_l')[:12]
    return render_to_response('index.html', locals())


def about(request, a):
    article_obj = Article.objects.get(id=a)
    article_obj.click_l += 1
    article_obj.save()
    return render_to_response('about.html', locals())


def listpic(request,met):
    article_obj=Article.objects.all()
    pag=Paginator(article_obj,8)
    pag_obj = pag.page(met)
    return render_to_response('listpic.html',locals())


def newslistpic(request, pag):
    article_get=request.GET.get('type')
    type_obj=type.objects.filter(name=article_get).first()
    print(type_obj)
    print(article_get)
    article_obj = type_obj.article.all()
    if len(article_obj)>5:
        c=5
    else:
        c=len(article_obj)
    paginator_obj = Paginator(article_obj, c)
    pag_obj = paginator_obj.page(pag)
    start = pag_obj.number - 2
    a=paginator_obj.count%5
    if a==0:
        b=paginator_obj.count//5
    else:
        b=paginator_obj.count//5+1
    if b>5:
        if start < 2:
            start = 1
            end = start + 5
        else:
            end = pag_obj.number + 3
            if end > paginator_obj.num_pages:
                end = paginator_obj.num_pages + 1
                start = end - 5
        pag_range = range(start, end)
    else:
        if start < 2:
            start = 1
        end=b+1
        pag_range=range(start, end)

    return render_to_response('newslistpic.html', locals())


def Setpassword(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result


def zhuce(request):
    return render(request, 'zhuce.html')


def zhuce1(request):
    massage = {'code': 1000, 'mag': ''}
    username = request.GET.get('form-username')
    flag = Yonghu.objects.filter(username=username).exists()
    if flag:
        massage = {'code': 1001, 'mag': '用户名已存在'}
    else:
        massage = {'code': 1000, 'mag': '可以使用该用户名'}
    return JsonResponse(massage)


def denglu(request):
    data = request.POST
    if data:
        username = data['form-username']
        password = data.get('form-password')
        md5 = hashlib.md5()
        md5.update(password.encode())
        setpassword = md5.hexdigest()
        falg = Yonghu.objects.filter(username=username).exists()
        falg1 = Yonghu.objects.filter(username=username).first()
        if falg:
            if falg1.password == setpassword:
                massage = '登录成功'
            else:
                massage = '密码错误'
        else:
            massage = '用户名不存在'
    return render(request, 'denglu.html', locals())


def seart(request,pag):
    content=request.GET.get('keyboard')
    pag=request.GET.get('pag',1)
    if content:
        pag_obj=Article.objects.filter(title__icontains=content).all()
        if len(pag_obj) > 5:
            c = 5
        else:
            c = len(pag_obj)
        paginator_obj = Paginator(pag_obj, c)
        pag_obj = paginator_obj.page(pag)
        start = pag_obj.number - 2
        a = paginator_obj.count % 5
        if a == 0:
            b = paginator_obj.count // 5
        else:
            b = paginator_obj.count // 5 + 1
        if b > 5:
            if start < 2:
                start = 1
                end = start + 5
            else:
                end = pag_obj.number + 3
                if end > paginator_obj.num_pages:
                    end = paginator_obj.num_pages + 1
                    start = end - 5
            pag_range = range(start, end)
        else:
            if start < 2:
                start = 1
            end = b + 1
            pag_range = range(start, end)

    return render(request,'newslistpic.html',locals())