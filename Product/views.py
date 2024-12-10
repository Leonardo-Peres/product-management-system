from dj_rql.drf import RQLFilterBackend

from rest_framework import viewsets

from Product.filters import ProductFilterClass, BrandFilterClass, CategoryFilterClass
from Product.models import Product, Brand, Category
from Product.serializers import ProductModelSerializer, BrandModelSerializer, CategoryModelSerializer


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    # django-rql ----------
    filter_backends = [RQLFilterBackend]
    rql_filter_class = ProductFilterClass


class BrandModelViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandModelSerializer
    # django-rql ----------
    filter_backends = [RQLFilterBackend]
    rql_filter_class = BrandFilterClass


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    # django-rql ----------
    filter_backends = [RQLFilterBackend]
    rql_filter_class = CategoryFilterClass
