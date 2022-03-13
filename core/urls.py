
from django.urls import path
import core.views
import core.models

app_name = 'core'

urlpatterns = [
    path('', core.views.index, name='index'),
    path('students/', core.views.student_list, name='student_list'),
    path('students/<int:pk>/', core.views.student_detail, name='student_detail'),
]
