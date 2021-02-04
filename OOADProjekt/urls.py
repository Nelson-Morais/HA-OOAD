"""OOADProjekt URL Configuration

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
from django.contrib import admin
from django.template.loader import get_template
from django.urls import path
from ShareCare.views.OfferView import OfferView
from ShareCare.views.RequestView import RequestView
from ShareCare.views.MessageView import MessageView


urlpatterns = [

    path('admin/', admin.site.urls),

    path('offer/',OfferView.getOffers ),
    path('offer/create', OfferView.create),
    # POST: =!=!)E§=)§)"?!?=?????????????????????


    path('request/create', RequestView.create),
    # POST

    # POST


    path('me/offer', OfferView.getPersonalOffers),
    path('me/incoming', RequestView.getIncomingRequests),
    path('me/outgoing', RequestView.getOutgoingRequest),
    path('me/messages', MessageView.getMessages)
]
