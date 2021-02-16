"""ShareCare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib import admin

from userauth import views as userauth_views
from pages.views import *
from bazaar.views import *
from notifications.views import *

urlpatterns = [
    # Pages
    path("", PageView.get_welcome, name="welcome"),

    # Bazaar
    path("offer/", get_offer_list, name="offer_list"),
    path("offer/create/", get_offer_creator, name="create_offer"),
    path("offer/<int:offer_id>/", get_offer, name="offer_details"),
    path("offer/<int:offer_id>/request/", get_request_creator, name="offer_request_creator"),
    #temp
    path("request/create/", get_request_creator, name="create_request"),


    # Personal Section
    path("me/offer/", get_personal_offer_list, name="personal_offer_list"),
    path("me/request/", get_personal_request_list, name="personal_request_list"),
    path("me/notifications/", get_notifications, name="notification_list"),
    #temp
    path("myrequests", temp_list, name="temp_list"),

    # UserAuth
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", userauth_views.signup, name="signup"),
    path('admin/', admin.site.urls)
]
