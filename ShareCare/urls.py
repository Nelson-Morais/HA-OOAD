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


Notification Interface for external Apps

@author Kevin Lucas Simon, Nelson Morais, Christina Bernhardt
Projekt OOAD Hausarbeit WiSe 2020/21

ShareCare URL Configuration

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

from apps.bazaar.views import OfferView, RequestView
from apps.notifications.views import NotificationView
from apps.pages.views import PagesView
from apps.userauth import views as userauth_views


urlpatterns = [
    # Pages
    path("", PagesView.get_welcome, name="welcome"),

    # Bazaar
    path("offer/", OfferView.offers_listing, name="offer_list"),
    path("offer/create/", OfferView.create_offer, name="create_offer"),
    path("offer/<int:offer_id>/", OfferView.get_offer, name="offer_details"),
    path("offer/<int:offer_id>/request/", RequestView.create_request, name="offer_request_creator"),

    # Personal Section
    path("me/offer/", OfferView.personal_offers_listing, name="personal_offer_list"),
    path("me/offer/delete/<int:offer_id>", OfferView.delete_offer, name="delete_offer"),
    path("me/offer/<int:offer_id>/accept/<int:request_id>", RequestView.accept_request, name="request_accept"),
    path("me/request/", RequestView.personal_request_listing, name="personal_request_list"),
    path("me/request/delete/<int:request_id>", RequestView.delete_request, name="delete_request"),
    path("me/notifications/", NotificationView.get_notifications, name="notification_list"),

    # UserAuth
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", userauth_views.signup, name="signup"),
    path('admin/', admin.site.urls)
]
