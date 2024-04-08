from rest_framework import routers
from Products.views import CategoryViewset, ProductViewset


router = routers.DefaultRouter()

router.register(r'categories', CategoryViewset)
router.register(r'products', ProductViewset)