from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Product.views import ProductModelViewSet, BrandModelViewSet, CategoryModelViewSet

router = DefaultRouter()
router.register('products', ProductModelViewSet)
router.register('brands', BrandModelViewSet)
router.register('categories', CategoryModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
