from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect, render
from accounts.forms import LoginForm, RegisterForm
from django.contrib import messages


def index(request):
    login_form = LoginForm(request=request)
    register_form = RegisterForm()
    next_url = request.GET.get('next') or request.POST.get('next') or "todo:index"
    active_tab = 'login'

    if "login_submit" in request.POST:
        active_tab = 'login'
        login_form = LoginForm(request=request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect(next_url)
        messages.error(request, f'Invalid username or password, please try again.!')
    elif "register_submit" in request.POST:
        active_tab = 'register'
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
            messages.success(request, f'Account created! Welcome, {user.username}!')
            return redirect(next_url)
        messages.error(request, f'Register failed! Please try again later.')
    return render(request, "auth.html",{
        "login_form": login_form,
        "register_form": register_form,
        "active_tab": active_tab,
        "next_url": next_url,
    })
