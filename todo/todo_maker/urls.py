
from django.urls import path, include
from todo_maker import views

app_name='todo_maker'
urlpatterns = [
    path('', views.List.as_view(),name="list-todo"),
    path('save', views.List.as_view(),name="save-todo"),
    path('edit/<int:pk>/', views.List.as_view(),name="edit-todo"),
    path('remove/<int:pk>/', views.List.as_view(),name="remove-todo"),
    path('task-completed', views.List.as_view(),name="todo-task-completed"),
]   