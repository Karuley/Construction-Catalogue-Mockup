import django_filters
from django_filters import CharFilter, RangeFilter
from .models import *



class ProductsFilter(django_filters.FilterSet):
    price_min = RangeFilter(field_name='price')
    name = CharFilter(field_name='name', lookup_expr='icontains')
    class Meta:
        model = Products
        fields = ('name', 'category', 'company')