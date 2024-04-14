from django.shortcuts import render
from rest_framework import viewsets
from .models import Categories, Product
from .serializers import CategoriesSerializer, ProductSerializer

# Create your views here.


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer



class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer




