import django_filters

import core.models


class StudentFilter(django_filters.FilterSet):
    lastName = django_filters.Filter(lookup_expr='icontains', label='Фамилия')
    group = django_filters.Filter(label='Группа')

    class Meta:
        model = core.models.Student
        fields = '__all__'
