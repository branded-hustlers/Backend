from rest_framework import serializers
# from .models import Cart, CartItem, Order, OrderedItem
# from Products.serializers import ProductSerializer
# from Customer.serializers import UserSerializer


# class CartItemSerializer(serializers.ModelSerializer):
#     Product = ProductSerializer

#     class Meta:
#         model = CartItem
#         fields = '__all__'








# class CartSerializer (serializers.ModelSerializer):
#     customer = UserSerializer()
#     items = CartItemSerializer(many = True, read_only=True)

#     class Meta:
#         model = Cart
#         fields = '__all__'

#     total_cost = serializers.SerializerMethodField()

#     def get_total_cost(self, obj):
#         return obj.total_cost
    



# class OrderedItemSerializer(serializers.ModelSerializer):
#     product = ProductSerializer
#     class Meta:
#         model = OrderedItem
#         fields = '__all__'




# class OrderSerializer(serializers.ModelSerializer):
#     item = OrderedItemSerializer(many=True, read_only=True)
#     class Meta:
#         model = Order
#         fields = '__all__'



# class CreateOrderSerializer(serializers.ModelSerializer):
#     cart = CartSerializer


#     def save(self, **kwargs):
#         return super().save(**kwargs)