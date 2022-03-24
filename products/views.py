from django.shortcuts import render
from products.models import Items
from rest_framework import generics
from .serializers import ItemsSerializer
# Create your views here.

class ItemsCreate(generics.CreateAPIView):
    #API endpoint that allows creation of a new item
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

class ItemsList(generics.ListAPIView):
    #API endpoint that allows list of items
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

class ItemsDetail(generics.RetrieveAPIView):
    #API endpoint that allows detail of items
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

class ItemsUpdate(generics.RetrieveUpdateAPIView):
    #API endpoint that allows an items to update
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

class ItemsDelete(generics.RetrieveDestroyAPIView):
     #API endpoint that allows an items to delete
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

