
from django.urls import path
import core.views
import core.models

app_name = 'core'

urlpatterns = [
    path('', core.views.IndexView.as_view(), name='index'),
    path('students/', core.views.Students.as_view(), name='student_list'),
    path('students/<int:pk>/', core.views.StudentDetail.as_view(), name='student_detail'),
    path('students/<int:pk>/update/', core.views.StudentUpdate.as_view(), name='student_update'),
    path('students/<int:pk>/delete/', core.views.StudentDelete.as_view(), name='student_delete'),
    path('students/create/', core.views.StudentCreate.as_view(), name='student_create'),
    path('home/fmiit', core.views.FMiIT.as_view(), name='core_fmiit'),
    path('home/ximfuk', core.views.XimFuk.as_view(), name='core_ximfuk'),
    path('home/iigu', core.views.IIGU.as_view(), name='core_iigu'),

]
