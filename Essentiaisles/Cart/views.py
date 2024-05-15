from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# from .models import Cart, Order
# from .serializers import CartSerializer,OrderSerializer, CreateOrderSerializer
from rest_framework.mixins import CreateModelMixin


# class CartViewSet(ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer

#     def get_queryset(self):
#         user = self.request.user
#         return Cart.objects.filter(customer=user)



# class OrderViewset(ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = OrderSerializer

#     def get_serializer_class(self):
#         if self.request.method == 'POST':
#             return super().get_serializer_class()
#         return OrderSerializer
    

#     def get_queryset(self):
#         user = self.request.user
#         if user.is_staff:
#             return Order.objects.all()
#         return Order.objects.filter(owner=user)