from django.views.generic import CreateView, UpdateView, FormView, ListView
from .models import Task, TaskForm, Comment, CommentForm
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.views.generic.edit import ModelFormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


# Create your views here.


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'tasks/index.html'
    model = Task

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id).prefetch_related('user')


class TaskDetailView(LoginRequiredMixin, DetailView):
    template_name = 'tasks/detail.html'
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CommentForm()
        context['comment_form'] = form
        return context


class CreateView(LoginRequiredMixin, CreateView):
    form_class = TaskForm
    model = Task

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)



class UpdateView(LoginRequiredMixin, UpdateView):
    form_class = TaskForm
    model = Task


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:index')


#################################################
#################################################


class CreateCommentView(LoginRequiredMixin, ModelFormMixin, FormView):
    template_name = 'tasks/detail.html'
    form_class = CommentForm
    model = Comment

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.task_id = self.kwargs['task']

        try:
            self.object.save()
            messages.success(self.request, 'Great ! Your comment has been added.')
        except:
            messages.warning(self.request, 'Oups ! Your comment hasn\'t been added.')

        return super().form_valid(form)

    def get_success_url(self):
        task_id = self.kwargs['task']
        return str(reverse_lazy('tasks:detail', kwargs={'pk': task_id}))


class DeleteCommentView(DeleteView):
    model = Comment

    def get_success_url(self):
        task_id = self.kwargs['task']
        try:
            messages.success(self.request, 'Comment deleted.')
        except:
            messages.warning(self.request, 'Oups ! Your comment hasn\'t been deleted.')

        return str(reverse_lazy('tasks:detail', kwargs={'pk': task_id}))


class UpdateCommentView(UpdateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        task_id = self.kwargs['task']
        return str(reverse_lazy('tasks:detail', kwargs={'pk': task_id}))
