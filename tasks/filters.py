from django_filters import rest_framework as filters
from .models import Task

class TaskFilter(filters.FilterSet):
    start_date = filters.DateFilter(field_name='date', lookup_expr='gte')
    end_date = filters.DateFilter(field_name='date', lookup_expr='lte')
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    
    class Meta:
        model = Task
        fields = ['start_date', 'end_date', 'title']
