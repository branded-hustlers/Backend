from rest_framework import serializers
from .models import Cart, CartItem
from Products.serializers import ProductSerializer
from Customer.serializers import CustomerSerializer


class CartItemSerializer(serializers.ModelSerializer):
    Product = ProductSerializer

    class Meta:
        model = CartItem
        fields = '__all__'








class CartSerializer (serializers.ModelSerializer):
    customer = CustomerSerializer()
    items = CartItemSerializer(many = True, read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'

    total_cost = serializers.SerializerMethodField()

    def get_total_cost(self, obj):
        return obj.total_cost