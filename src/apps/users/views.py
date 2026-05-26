from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from .forms import LoginForm, RegisterForm



def login_page(request: HttpRequest):
    form = LoginForm()

    if request.method == "POST":
        
        form = LoginForm(request.POST)
        
        if form.is_valid():
            user = authenticate(
                request,
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
        
            if user is None:
                form.add_error(None, 'Invalid email or password.')
        
            else:
                login(request, user)
                return redirect('apps.landing:landing_page')

    return render(request, 'login.html', {'form': form})


def register_page(request: HttpRequest):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
        
            user = form.save()
        
            login(request, user)
            return redirect('apps.landing:landing_page')

    return render(request, 'register.html', {'form': form})




def logout_page(request: HttpRequest):
    
    logout(request)
    
    return redirect('apps.landing:landing_page')
    




