from django.shortcuts import redirect, render, get_object_or_404
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from products.models import Items
from rest_framework import generics
from .serializers import ItemsSerializer
from rest_framework.views import APIView
# Create your views here.

class ItemsCreate(generics.CreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "products/product_create.html"

    def get(self, request):
        product = get_object_or_404(Items)
        serializer = ItemsSerializer(product)
        return Response({'serializer': serializer, 'product':product})
    
    def post(self, request):
        product = get_object_or_404(Items)
        serializer = ItemsSerializer(product, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer':serializer,'product':product})
        serializer.save()
        return redirect('products:item_list')
    # #API endpoint that allows creation of a new item
    # queryset = Items.objects.all()
    # serializer_class = ItemsSerializer

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

