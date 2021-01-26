from django.shortcuts import render, redirect, get_object_or_404
from .forms import todo_modelForm
from .models import todo_model
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'todo/home.html')


@login_required(login_url='user_login')
def current_todo(request):
    todos = todo_model.objects.filter(
        user=request.user, Completed_time__isnull=True)
    return render(request, 'todo/current_to-do.html', {'todos': todos})


@login_required(login_url='user_login')
def createTodo(request):
    if request.method == 'GET':
        return render(request, 'todo/createTodo.html', {'form': todo_modelForm()})
    else:
        try:
            form = todo_modelForm(request.POST)
            newToDo = form.save(commit=False)
            newToDo.user = request.user
            newToDo.save()
            return redirect('/todo/current')
        except ValueError:
            return render(request, 'todo/createTodo.html', {'form': todo_modelForm(), 'error': 'Sorry, Bad Data Passed In! Try again correctly.'})


@login_required(login_url='user_login')
def viewTodo(request, todo_pk):
    todos = get_object_or_404(todo_model, pk=todo_pk, user=request.user)
    if request.method == 'GET':
        form = todo_modelForm(instance=todos)
        return render(request, 'todo/view_to-do.html', {'todos': todos, 'form': form})
    else:
        try:
            form = todo_modelForm(request.POST, instance=todos)
            form.save()
            return redirect('/todo/current')
        except ValueError:
            return render(request, 'todo/createTodo.html', {'form': todo_modelForm(), 'error': 'Sorry, Bad Data Passed In! Try again correctly.'})


@login_required(login_url='user_login')
def completeTodo(request, todo_pk):
    todos = get_object_or_404(todo_model, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todos.Completed_time = timezone.now()
        todos.save()
        return redirect('/todo/current')


@login_required(login_url='user_login')
def deleteTodo(request, todo_pk):
    print("before if condition")
    todos = get_object_or_404(todo_model, pk=todo_pk, user=request.user)
    
    if request.method == 'POST':
        print("after if condition and before delete")
        todos.delete()
        print("before redirecting")
        return redirect('/todo/current')


@login_required(login_url='user_login')
def completed_todo(request):
    todos = todo_model.objects.filter(
        user=request.user, Completed_time__isnull=False).order_by('-Completed_time')
    return render(request, 'todo/completed_to-do.html', {'todos': todos})
