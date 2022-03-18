from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView

import core.models
import core.forms
import core.filters

class TitleMixin:
    title:str = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = self.get_title()
        return context


class IndexView(TitleMixin, TemplateView):
    template_name = 'core/index.html'
    title = 'Главная страница'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['info'] = self.get_info()
        return context

    def get_info(self):
        return 'Главная страница'


class Students(TitleMixin, ListView):
    title = 'Студенты'

    def get_filters(self):
        return core.filters.StudentFilter(self.request.GET)

    def get_queryset(self):
        # lastname = self.request.GET.get('lastname')
        # queryset = core.models.Student.objects.all()
        # if lastname:
        #     queryset = queryset.filter(lastName__icontains=lastname)
        return self.get_filters().qs

    def get_context_data(self):
        context = super().get_context_data()
        context['form'] = core.forms.StudentSearch(self.request.GET or None)
        # context['filters'] = self.get_filters()
        return context


class StudentDetail(TitleMixin, DetailView):
    queryset = core.models.Student.objects.all()

    def get_title(self):
        return str(self.get_object())


class StudentUpdate(TitleMixin, UpdateView):
    model = core.models.Student
    form_class = core.forms.StudentEdit

    def get_title(self):
        return f'Изменение данных студента "{str(self.get_object())}"'

    def get_success_url(self):
        return reverse('core:student_list')


class StudentCreate(TitleMixin, CreateView):
    model = core.models.Student
    form_class = core.forms.StudentEdit
    title = 'Добавление студента'

    def get_success_url(self):
        return reverse('core:student_list')


class StudentDelete(TitleMixin, DeleteView):
    model = core.models.Student

    def get_title(self):
        return f'Удаление студента {str(self.get_object())}'

    def get_success_url(self):
        return reverse('core:student_list')
