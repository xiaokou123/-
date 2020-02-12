from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http.response import HttpResponse
# Create your views here.
def lian(request):
    return render_to_response('lian.html')