from django.urls import path
from .views import LoginView, TodoListView

urlpatterns = [
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/todos/', TodoListView.as_view(), name='todo-list'),
]
