from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer

from django_filters import rest_framework as filters
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend)
    search_fields = ['title', 'description']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filterset_fields = ['products']
    filter_backends = (filters.DjangoFilterBackend)