from django.urls import path,re_path
from .views import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.routers import SimpleRouter
router=SimpleRouter()
router.register(r'API/Goods',GoodsViews)

urlpatterns = [
    path("gettoken/",gettoken)
]