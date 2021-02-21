from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from .forms import CreateUser, LoginForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, "You are Signed up, Plz Login!")
            return redirect('loginapp:login')
        else:
            messages.error(request, "Plz SigneUp again!")
    else:
        form = CreateUser()
    return render(request, 'loginapp/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                #messages.success(request,'Successfully Logged In')
                return redirect('loginapp:home')
    else:
        form = LoginForm()
    return render(request, 'loginapp/login.html', {'form': form})


def home(request):
    return render(request, 'loginapp/dashboard.html')
