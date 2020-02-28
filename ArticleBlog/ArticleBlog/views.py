from django.http import HttpResponse
from django.shortcuts import render_to_response,render
from app01.models import *


def addauthor(request):
    # aut=author(name='张三',gender='男',age=27,email='123456@qq.com')
    # aut.save()
    # author.objects.create(name='李四',gender='男',age=28,email='246243@qq.com')
    # author.objects.create(name='王五',gender='女',age=24,email='635423@qq.com')
    # author.objects.create(name='铁锤',gender='女',age=33,email='855345@qq.com')
    # author.objects.create(name='赵六',gender='男',age=37,email='423463@qq.com')
    return HttpResponse("add author")

def addArticle(request):
    # author_obj=author.objects.filter(name='王五').first()
    # author_obj=author.objects.filter(name='张三').first()
    # author_obj=author.objects.filter(name='李四').first()
    # author_obj=author.objects.filter(name='铁锤').first()
    # author_obj=author.objects.filter(name='赵六').first()
    # Article.objects.create(title='可爱的欢欢',date='2019-03-22',content='可及时付款计',description='休闲',author=author_obj)
    # author_obj.article_set.create(title='大话水浒',date='2019-06-07',content='收到贵司的',description='神话')
    # author_obj.article_set.create(title='隋唐演义',date='2018-07-03',content='收杀杀杀的',description='名著')
    # author_obj.article_set.create(title='战国传',date='2018-12-22',content='撒地方大师傅',description='名著')
    # author_obj.article_set.create(title='穿越到唐朝',date='2017-01-09',content='手动阀手动阀',description='穿越')
    # author_obj.article_set.create(title='附身李白',date='2016-11-11',content='是个十分士大夫',description='穿越')
    return HttpResponse('add Article')
def addtype(request):
    # type.objects.create(name='休闲',description='谁给我个')
    # type.objects.create(name='神话',description='是个十分')
    # type.objects.create(name='名著',description='获得更好的发')
    # type.objects.create(name='穿越',description='好的法国队')


    return HttpResponse("add type")
def addkey(request):
    # type_obj=type.objects.filter(name='穿越').first()
    # article_obj = Article.objects.filter(description='神话')
    # print(article_obj)
    # for i in article_obj:
    #     # type_obj.article.add(i)
    #     i.type_set.add(type_obj)
    return HttpResponse('增加多对多外键')



def getall(request):
    author_obj = author.objects.get(name='张三').article_set.all()
    for i in author_obj:
        print(i.title,i.date)
        i_obj=i.type_set.all()
        for j in i_obj:
            print(j.name,end=" ")
        print()


    return HttpResponse('获取数据')
def deleteall(request):


    return HttpResponse('删除')