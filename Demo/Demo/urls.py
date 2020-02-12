"""Demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^$',index),
    path('index/',index),
    re_path('index.html$',index),
    path('about/',about),
    re_path('about.html$',about),
    path('listpic/',listpic),
    re_path('listpic.html$', listpic),
    path('newslistpic/',newslistpic),
    re_path('newslistpic.html$', newslistpic),
    path('getindex/',getindex),
    path('getindex1/',getindex1)
]
