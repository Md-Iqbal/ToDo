from django.urls import include, path
from .import views

urlpatterns = [
    #authentication related link
    path('', views.home, name='home'),
    path('todo/current/', views.current_todo, name='current_todo'),
    path('todo/completed/', views.completed_todo, name='completed_todo'),
    path('createTodo/', views.createTodo, name='createTodo'),
    path('todo/<int:todo_pk>', views.viewTodo, name='viewTodo'),
    path('todo/<int:todo_pk>/complete', views.completeTodo, name='completeTodo'),
    path('todo/<int:todo_pk>/delete', views.deleteTodo, name='deleteTodo'),

]
