from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.shortcuts import render
def index(request):
    return render_to_response('index.html')
def listpic(request):
    return render_to_response('listpic.html')
def newslistpic(request):
    return render_to_response('newslistpic.html')

def about(request):
    return render_to_response('about.html')

def getindex(request):
    template_obj=get_template('index1.html')
    params={'name':'古天乐','age':45}
    result=template_obj.render(params)
    return HttpResponse(result)
# def getindex1(request):
#     params={'name':'古天乐','age':20}
#     return render(request,'index1.html',params)
def getindex1(request):
    import time,datetime
    name='gtl'
    age=40
    hobby=['唱歌','跳舞','打篮球']
    score={'python':100,'java':90,'php':80}
    subject=('python','java','php')
    # now_time=time.strftime("%Y-%m-%d %H:%M:%S")
    now_time=datetime.datetime.now()\
        # .strftime("%Y-%m-%d %H:%M:%S")
    return render(request,'index1.html',locals())
