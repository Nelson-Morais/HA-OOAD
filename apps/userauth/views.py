"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.


Defines custom Signup Forms

Used Tutorial: https://grokonez.com/django/django-authentication-login-example-logout-signup-for-custom-user-tutorial

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
