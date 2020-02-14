from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http.response import HttpResponse
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
