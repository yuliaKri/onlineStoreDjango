import django_filters
from .models import Product

class ProductFilter(django_filters.rest_framework.FilterSet): # django_filters
    brand = django_filters.CharFilter(field_name='brand__title', lookup_expr='contains')
    title = django_filters.CharFilter(field_name='title', lookup_expr='contains')
    brand_id = django_filters.NumberFilter(field_name='brand__id', lookup_expr='exact')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte') # >= if 'gt' then >
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte') # <=
    # example: http://127.0.0.1:8000/api/product/all/?brand_id=1&min_price=20&max_price=150
    class Meta:
        model = Product
        fields = ['brand', 'title', 'min_price', 'max_price']