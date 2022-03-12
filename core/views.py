from django.http import HttpResponse
from django.shortcuts import render
import core.models


def index(request):
    students = core.models.Student.objects.all()
    return render(request, 'core/index.html', {'students': students})
