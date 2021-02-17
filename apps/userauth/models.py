"""
Django additional User data Model

Used Tutorial: https://grokonez.com/django/django-authentication-login-example-logout-signup-for-custom-user-tutorial

@author Kevin Lucas Simon, Nelson Morais, Christina Bernhardt
Projekt OOAD Hausarbeit WiSe 2020/21
"""
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    """Describes the CustomUser Model"""
    full_name = models.CharField(max_length=100, blank=False)
