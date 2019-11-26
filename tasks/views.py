from django.views.generic import CreateView, TemplateView, UpdateView, FormView
from .models import Task, TaskForm, Comment, CommentForm
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.views.generic.edit import ModelFormMixin

# Create your views here.


class IndexView(TemplateView):
    template_name = 'tasks/index.html'
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context


class TaskDetailView(DetailView):
    template_name = 'tasks/detail.html'
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        form = CommentForm()
        context['comment_form'] = form
        return context


class CreateView(CreateView):
    form_class = TaskForm
    model = Task


class UpdateView(UpdateView):
    form_class = TaskForm
    model = Task


class DeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:index')


#################################################
#################################################


class CreateCommentView(ModelFormMixin, FormView):
    template_name = 'tasks/detail.html'
    form_class = CommentForm
    model = Comment

    def form_valid(self, form):
        form.instance.task_id = self.kwargs['task']
        return super().form_valid(form)

    def get_success_url(self):
        task_id = self.kwargs['task']
        return str(reverse_lazy('tasks:detail', kwargs={'pk': task_id}))


class DeleteCommentView(DeleteView):
    model = Comment

    def get_success_url(self):
        task_id = self.kwargs['task']
        return str(reverse_lazy('tasks:detail', kwargs={'pk': task_id}))


class UpdateCommentView(UpdateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        task_id = self.kwargs['task']
        return str(reverse_lazy('tasks:detail', kwargs={'pk': task_id}))
