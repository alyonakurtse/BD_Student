from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView, ListView, DetailView

import core.models


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

    def get_queryset(self):
        lastname = self.request.GET.get('lastname')
        queryset = core.models.Student.objects.all()
        if lastname:
            queryset = queryset.filter(lastName__icontains=lastname)
        return queryset


class StudentDetail(TitleMixin, DetailView):
    queryset = core.models.Student.objects.all()

    def get_title(self):
        return str(self.get_object())

