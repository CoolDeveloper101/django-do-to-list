from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('delete_todo/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('completed_todo/<int:todo_id>/', views.completed_todo, name='completed_todo'),
]