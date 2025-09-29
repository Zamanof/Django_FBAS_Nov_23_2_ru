from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('<int:task_id>', views.detail, name='detail'),
]