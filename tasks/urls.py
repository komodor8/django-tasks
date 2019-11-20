from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('create/', views.CreateView.as_view(), name='create'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('store/', views.store, name='store'),
    path('delete/<int:pk>', views.TaskDeleteView.as_view(), name='delete'),
]
