from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from .models import Task, TaskForm
from . import forms
from django.http import HttpResponse
import web_pdb
from django.views.generic.detail import DetailView, SingleObjectMixin


# Create your views here.


class IndexView(TemplateView):
    template_name = 'tasks/index.html'
    model = Task

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        # web_pdb.set_trace()
        print('context =>', context)
        context['tasks'] = Task.objects.all()
        return context


class DetailView(DetailView):
    template_name = 'tasks/detail.html'
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        web_pdb.set_trace()
        print(context['object'])
        return context


class CreateView(TemplateView):
    template_name = 'tasks/create.html'
    model = Task


def store(request):
    # print(request.POST)
    newTask = Task()
    f = TaskForm(request.POST, instance=newTask)
    f.save()
    return redirect('/tasks', permanent=True)
