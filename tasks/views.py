from django.shortcuts import redirect, render
from django.views.generic import CreateView, TemplateView, UpdateView, FormView
from .models import Task, TaskForm, Comment, CommentForm
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import DeleteView
from django.views.generic.detail import SingleObjectMixin
from django.views import View
from django.views.generic.edit import ModelFormMixin

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
        form = CommentForm()
        context['comment_form'] = form
        return context


class CreateCommentView(ModelFormMixin, FormView):
    template_name = 'tasks/detail.html'
    form_class = CommentForm
    model = Task

    def get_form_kwargs(self):
        o = super().get_form_kwargs()
        o['instance'] = Comment(task = self.get_object())
        return o

    def get_success_url(self):
        return reverse('tasks:detail', kwargs={'pk': self.get_object().pk})


class TaskDetailView(View):

    def get(self, request, *args, **kwargs):
        view = DetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CreateCommentView.as_view()
        return view(request, *args, **kwargs)


class CreateView(CreateView):
    form_class = TaskForm
    model = Task


class UpdateView(UpdateView):
    form_class = TaskForm
    model = Task


class DeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:index')
