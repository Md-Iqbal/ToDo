from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
# from django.http import HttpResponse

# Create your views here.


def user_signup(request):
    if request.method == 'GET':
        return render(request, 'authentication/user_signup.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password2'])
                user.save()
                login(request, user)
                return redirect('/todo/current')
            except IntegrityError:
                return render(request, 'authentication/user_signup.html', {'form': UserCreationForm(), 'error': 'Sorry username has already been taken. Choose another one!!!'})
        else:
            return render(request, 'authentication/user_signup.html', {'form': UserCreationForm(), 'error': 'Password did not match!!!'})


def user_login(request):
    if request.method == 'GET':
        return render(request, 'authentication/user_login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'authentication/user_login.html', {'form': AuthenticationForm(), 'error': 'Sorry, Username and Password did not match! Try Again.'})
        else:
            login(request, user)
            return redirect('/todo/current')


def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
