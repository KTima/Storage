from attr import fields
import django_filters
from .models import *

class SalariesFilter(django_filters.FilterSet):
    class Meta:
        model = Salaries
        fields = ['Year','Month']