from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import User
from .forms import LoginFrom,UserCreationForm
# Create your views here.

def user_register(request):
    context = {}
    if request.method == 'GET':
        context['form'] = UserCreationForm()
        return render(request, 'accounts/register.html', context)
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            return redirect('login')
        else:
            messages.error(request, 'Registration failed')
            context['form'] = form
            return render(request, 'accounts/register.html', context)


def user_login(request):
    context = {}
    if request.method == 'GET':
        context['form'] = LoginFrom()
        return render(request, 'accounts/login.html', context)
    elif request.method == 'POST':
        form = LoginFrom(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse(f'user login successful 9username : {username})')
            else:
                return HttpResponse('Login failed')
            
         # If the form is not valid.
        context['form'] = form
        return render(request, 'accounts/login.html', context)
