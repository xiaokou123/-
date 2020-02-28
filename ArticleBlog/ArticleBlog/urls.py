"""ArticleBlog URL Configuration

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
from django.urls import path,include,re_path
from .views import *
# from django.conf.urls.static import static   #解决富文本不能上传图片
# from . import settings    #解决富文本不能上传本地图片
from app01.views import *
urlpatterns = [
    # re_path(r'ckeditor/',include('ckeditor_uploader')),   #解决富文本不能上传本地图片
    path('admin/', admin.site.urls),
    path('app01/',include('app01.urls')),
    path('addauthor/',addauthor),
    path('addArticle/',addArticle),
    path('addtype/',addtype),
    path('addkey/',addkey),
    path('getall/',getall),
    re_path('^$',index),

]
# urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)   #解决富文本不能上传本地图片