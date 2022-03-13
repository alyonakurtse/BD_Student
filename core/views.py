from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods

import core.models


def index(request):
    students = core.models.Student.objects.all()
    return render(request, 'core/index.html', {'students': students})


def student_list(request):
    students = core.models.Student.objects.all()
    return render(request, 'core/student_list.html', {'students': students})


def student_detail(request, pk):
    student = get_object_or_404(core.models.Student, pk=pk)
    return render(request, 'core/student_detail.html', {'student': student})

