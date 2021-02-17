"""
Notification Interface for external Apps

@author Kevin Lucas Simon, Nelson Morais, Christina Bernhardt
Projekt OOAD Hausarbeit WiSe 2020/21
"""
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm


def signup(request):
    """
    defines the Signup Form
    :param request: HTTP Request
    :return: redirects to a page
    """
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect("welcome")
    else:
        form = SignUpForm()

    return render(request, "signup.html", {
        "form": form
    })
