from rest_framework import serializers
from .models import Categories, Product


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__' 

class ProductSerializer(serializers.ModelSerializer):
    Category = CategoriesSerializer
    
    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'description', 'price', 'image')
