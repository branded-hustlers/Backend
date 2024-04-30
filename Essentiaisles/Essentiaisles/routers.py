from django.urls import path, include
from rest_framework import routers
from Products.views import ProductViewset, CategoryViewset, ProductReviewViewset



router = routers.DefaultRouter()
router.register(r'Category', CategoryViewset)
router.register(r'Product', ProductViewset)
router.register(r'ProductReview', ProductReviewViewset)


urlpatterns = [
    path('', include(router.urls))
]
