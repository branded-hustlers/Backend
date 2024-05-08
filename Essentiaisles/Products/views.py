from django.http import JsonResponse, Http404
from django.views import View
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination


class ProductView(APIView):
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10



    def get(self, request,*args, **kwargs):
        product_id = kwargs.get('pk')
        if product_id:
            try:
                product = Product.objects.get(pk=product_id)
                serializer = ProductSerializer(product)
                return JsonResponse(serializer.data, status=200)
            except Product.DoesNotExist:
                return JsonResponse({'error': 'Product not found.'}, status=404)
        else:
            paginator = self.pagination_class()
            products = Product.objects.all()
            result_page = paginator.paginate_queryset(products, request)
            serializer = ProductSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    


    


class CategoryView(View):
    def get(self, request, **kwargs):
        category_id = kwargs.get('pk')
        if category_id:
            try:
                category = Category.objects.get(pk=category_id)
                serializer = CategorySerializer(category)
                return JsonResponse(serializer.data, status=200)
            except Category.DoesNotExist:
                return JsonResponse({'error': 'Category does not exist'}, status=404)
        else:
            categories=Category.objects.all()
            serializer=CategorySerializer(categories, many=True)
            return JsonResponse(serializer.data, status=200, safe=False)