from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from .models import Task, TaskForm
from . import forms
from django.http import HttpResponse
import web_pdb
from django.views.generic.detail import DetailView, SingleObjectMixin
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


class CreateView(TemplateView):
    template_name = 'tasks/create.html'
    model = Task


def store(request):
    newTask = Task()
    f = TaskForm(request.POST, instance=newTask)
    f.save()
    return redirect('/tasks', permanent=True)


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:index')
