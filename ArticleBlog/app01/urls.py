from django.contrib import admin
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index),
    # path('seart/',seart),
    re_path('^$',index),
    re_path('about/(?P<a>\d+)',about),
    re_path('newslistpic/(?P<pag>\d+)', newslistpic),
    re_path('listpic/(?P<met>\d+)',listpic),
    re_path('seart/(?P<pag>\d+)',seart),
    path('zhuce/',zhuce),
    path('zhuce1/',zhuce1),
    path('denglu/',denglu),

]