from rest_framework import serializers
from products.models import Items

class ItemsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Items
        fields = ['id','name','price','product_image','quantity']