from rest_framework import serializers
from .models import Category, Product, ProductReview, Inventory

"""
serializer for category model
"""
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

"""
serializer for product model
"""

class ProductSerializer(serializers.ModelSerializer):
    Category = CategorySerializer

    class Meta:
        model = Product
        fields = '__all__'

"""
serializer for productReview model
"""


class ProductReviewSerializer(serializers.ModelSerializer):
    Product = ProductSerializer
    
    class Meta:
        model = ProductReview
        fields = '__all__'

"""
serializer for inventory model
"""

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'