from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('<int:pk>/', views.TaskDetailView.as_view(), name='detail'),
    path('update/<int:pk>', views.UpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.DeleteView.as_view(), name='delete'),
    path(
        '<int:task>/comments/create',
        views.CreateCommentView.as_view(),
        name='comments-create'
    ),
    path(
        '<int:task>/comments/<int:pk>/delete/',
        views.DeleteCommentView.as_view(),
        name='comments-delete'
    ),
    path(
        '<int:task>/comments/<int:pk>/update/',
        views.UpdateCommentView.as_view(),
        name='comments-update'
    ),
]
