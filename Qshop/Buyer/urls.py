from django.urls import path,include,re_path
from .views import *
urlpatterns = [
    path('index/',index),
    path('login/',login),
    path('register/',register),
]
