from rest_framework import serializers
from .models import User, Category, Product, Cart


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'name')
        extra_kwargs = {'password': {'write_only':True}}



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer
    
    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'description', 'price', 'image')



class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer
    product = ProductSerializer

    class Meta:
        model = Cart
        fields = ('id', 'user', 'product', 'total')