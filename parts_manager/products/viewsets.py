from rest_framework import viewsets, filters
from parts_manager.products.models import Product, Retailer
from parts_manager.products.serializers import (
    ProductSerializer,
    RetailerSerializer
)


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (
        filters.SearchFilter,
    )
    search_fields = ('item__name', 'retailer__name')


class RetailerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows retailers to be viewed or edited.
    """
    queryset = Retailer.objects.all()
    serializer_class = RetailerSerializer
    filter_backends = (
        filters.SearchFilter,
    )
    search_fields = ('name', )
