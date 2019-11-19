from django.contrib import admin

# Register your models here.
from .models import Task


class TaskAdmin(admin.ModelAdmin):

    model = Task

    fieldsets = [
        ('task_name', {
            'fields': ['task_name']
        }),
        ('task_description', {
            'fields': ['task_description']
        }),
        ('task_is_done', {
            'fields': ['task_is_done']
        }),
        ('task_due_date', {
            'fields': ['task_due_date']
        }),
        ('pub_date', {
            'fields': ['pub_date']
        }),
    ]


admin.site.register(Task, TaskAdmin)
