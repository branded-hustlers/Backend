from django.urls import path
from .views import ProductView, CategoryView

urlpatterns=[
    path('Product/', ProductView.as_view(), name='product-list'),
    path('Category/', CategoryView.as_view, name='category-list')
]