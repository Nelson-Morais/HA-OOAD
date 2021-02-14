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
    path("offer", OfferView.get_offer_list, name="offer_list"),
    path("offer/create", OfferView.get_offer_creator, name="offer_creator"),
    path("offer/<int:offer_id>", OfferView.get_offer, name="offer_details"),
    path("offer/<int:offer_id>/request", RequestView.save_request_creator, name="offer_request_creator"),

    # Personal Section
    path("me/offer", OfferView.get_personal_offer_list, name="personal_offer_list"),
    path("me/request", RequestView.get_personal_request_list, name="personal_request_list"),
    path("me/notifications", MessageView.get_notifications, name="notification_list"),

    # UserAuth
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", userauth_views.signup, name="signup"),
    path('admin/', admin.site.urls),
]
