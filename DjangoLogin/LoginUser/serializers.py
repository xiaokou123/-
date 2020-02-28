from rest_framework import serializers
from .models import *

class GoodsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Goods
        fields=["id","goods_number","goods_name","goods_price","goods_count","goods_location","goods_safe_date","state"]