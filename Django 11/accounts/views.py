from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render
from .forms import LoginForm, RegisterForm

def auth_view(request):
    login_form = LoginForm(request=request)
    register_form = RegisterForm()
    next_url = request.GET.get("next") or request.POST.get("next") or "todo:index"
    active_tab = "login"

    if "login_submit" in request.POST:
        active_tab = "login"
        login_form = LoginForm(request=request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect(next_url)
        messages.error(request, "Invalid username or password.")

    elif "register_submit" in request.POST:
        active_tab = "signup"
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
            messages.success(request, f"Account created! Welcome, {user.username}!")
            return redirect(next_url)
        messages.error(request, "Registration failed. Please check the form.")

    return render(request, "auth.html", {
        "login_form": login_form,
        "register_form": register_form,
        "active_tab": active_tab,
        "next": next_url,
    })
