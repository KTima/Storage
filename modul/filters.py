import django_filters
from .models import *

class IngredinetsFilter(django_filters.FilterSet):

    class Meta:
        model = Ingredients
        fields = ['Product']