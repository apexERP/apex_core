from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm, ProfileForm, PasswordChangeForm



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


@login_required(login_url='apps.users:login')
def profile_page(request: HttpRequest):
    profile_form = ProfileForm(instance=request.user)
    password_form = PasswordChangeForm(user=request.user)

    if request.method == 'POST':
        if 'update_profile' in request.POST:
            profile_form = ProfileForm(request.POST, instance=request.user)
            if profile_form.is_valid():
                profile_form.save()
                return redirect('apps.users:profile')

        elif 'change_password' in request.POST:
            password_form = PasswordChangeForm(user=request.user, data=request.POST)
            if password_form.is_valid():
                request.user.set_password(password_form.cleaned_data['new_password'])
                request.user.save()
                login(request, request.user)
                return redirect('apps.users:profile')

    return render(
        request, 
        'profile.html', 
        context = {
            'profile_form': profile_form,
            'password_form': password_form,
        }
    )
    




