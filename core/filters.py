from django_filters import filters

import core.models


class StudentFilter(filters.Filter):
    lastname = filters.Filter()

    class Meta:
        model = core.models.Student
        fields = ('lastname', )
