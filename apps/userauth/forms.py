from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, help_text="Maximal 100 Zeichen.")

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("full_name",)
