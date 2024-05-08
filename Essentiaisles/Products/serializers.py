from rest_framework import serializers
from .models import Category, Product, ProductReview, Inventory

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    Category = CategorySerializer

    class Meta:
        model = Product
        fields = '__all__'



class ProductReviewSerializer(serializers.ModelSerializer):
    Product = ProductSerializer
    
    class Meta:
        model = ProductReview
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'