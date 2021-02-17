"""
Django Custom SignUpForm

Used Tutorial: https://grokonez.com/django/django-authentication-login-example-logout-signup-for-custom-user-tutorial

@author Kevin Lucas Simon, Nelson Morais, Christina Bernhardt
Projekt OOAD Hausarbeit WiSe 2020/21
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class SignUpForm(UserCreationForm):
    """Describes the SIGN UP Form"""
    full_name = forms.CharField(max_length=100, help_text="Maximal 100 Zeichen.")

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("full_name",)
