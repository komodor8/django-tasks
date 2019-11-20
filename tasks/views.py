from django.shortcuts import redirect, render
from django.views.generic import CreateView, TemplateView, UpdateView
from .models import Task, TaskForm
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

# Create your views here.


class IndexView(TemplateView):
    template_name = 'tasks/index.html'
    model = Task

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context


class DetailView(DetailView):
    template_name = 'tasks/detail.html'
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        print(context['tasks'])
        return context


class CreateView(CreateView):
    form_class = TaskForm
    model = Task


class UpdateView(UpdateView):
    form_class = TaskForm
    model = Task


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:index')
