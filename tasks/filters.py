import django_filters

from .models import Task

class TaskFilter(django_filters.FilterSet):

    name = django_filters.CharFilter(lookup_expr='icontains', label='name')
    description = django_filters.CharFilter(lookup_expr='icontains', label='description', method='filter_description')
    due_date = django_filters.DateFilter()
    created_at = django_filters.DateFilter()

    def filter_description(self, queryset, name, value):
        return queryset.filter()

    class Meta:
        model = Task
        fields = ['name', 'description', 'due_date', 'created_at']
