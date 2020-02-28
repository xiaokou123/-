from django.contrib import admin
from django.urls import path,include,re_path
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',register ),
    path('login/',login ),
    re_path('^$',index ),
    path('goods_all/',goods_all ),
    path('del_cookies/',del_cookies ),
    path('goods_state/',goods_state ),
    path('goods_add/',goods_add ),
    path('seek/',seek ),
    path('user_profile/',user_profile ),
    re_path('goods_all/(?P<page>\d+)/(?P<status>\d+)', goods_all),
    re_path('goods_state/(?P<id>\d+)/(?P<state>\w+)/(?P<page>\d+)', goods_state),
]