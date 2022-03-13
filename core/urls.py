
from django.urls import path
import core.views
import core.models

app_name = 'core'

urlpatterns = [
    path('', core.views.IndexView.as_view(), name='index'),
    path('students/', core.views.Students.as_view(), name='student_list'),
    path('students/<int:pk>/', core.views.StudentDetail.as_view(), name='student_detail'),
]
