from django.db import models
from django.forms import DateTimeField, ModelForm
from django.urls import reverse
from django.forms.widgets import DateInput


# Create your models here.


class DateInput(DateInput):
    input_type = 'date'


class Task(models.Model):
    task_name = models.CharField(max_length=50)
    task_description = models.CharField(max_length=200)
    task_is_done = models.BooleanField(default=False)
    task_due_date = models.DateTimeField('date task')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.task_name

    def get_absolute_url(self):
        return reverse('tasks:detail', args=[str(self.id)])


class TaskForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["task_name"].widget.attrs['class'] = 'bg-red'

    task_due_date = DateTimeField(widget=DateInput)
    pub_date = DateTimeField(widget=DateInput)

    class Meta:
        model = Task
        fields = [
            'task_name',
            'task_description',
            'task_is_done',
            'task_due_date',
            'pub_date'
        ]


class Comment(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    task = models.ForeignKey('Task', on_delete=models.CASCADE)


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = [
            'title',
            'description'
        ]
