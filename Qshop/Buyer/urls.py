from django.urls import path,include,re_path
from .views import *
urlpatterns = [
    path('index/',index),
    path('login/',login),
    path('register/',register),
    path('alipay_ordeer/',alipay_ordeer),
    path('pay_resutl/',pay_resutl),
    path('del_payorder/',del_payorder),
    re_path('del_payorder/(?P<state>\d*)',del_payorder),
    path('xiazai/',xiazai),
    path('add_cart/',add_cart),
    path('operation/',operation),
    path('cart_place_order/',cart_place_order),
    path('center_place_order/',center_place_order),
    path('set_state/',set_state),
]
