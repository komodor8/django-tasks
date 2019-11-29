from django.db import models
from django.forms import DateTimeField, ModelForm
from django.urls import reverse
from django.forms.widgets import DateInput
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.


class DateInput(DateInput):
    input_type = 'date'


class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    due_date = models.DateTimeField()
    created_at = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tasks:detail', args=[str(self.id)])


class TaskForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs['class'] = 'bg-red'

    due_date = DateTimeField(widget=DateInput)

    class Meta:
        model = Task
        fields = [
            'name',
            'description',
            'is_done',
            'due_date',
        ]


class Comment(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    task = models.ForeignKey('Task', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = [
            'title',
            'description'
        ]
