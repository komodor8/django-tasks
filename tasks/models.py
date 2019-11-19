from django.db import models
from django.forms import ModelForm

# Create your models here.


class Task(models.Model):
    task_name = models.CharField(max_length=50)
    task_description = models.CharField(max_length=200)
    task_is_done = models.BooleanField(default=False)
    task_due_date = models.DateTimeField('date task')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.task_name


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            'task_name',
            'task_description',
            'task_is_done',
            'task_due_date',
            'pub_date'
        ]
