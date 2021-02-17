"""
PagesView controls the normal Pages of the System

@author Kevin Lucas Simon, Christina Bernhardt ,Nelson Morais
Projekt OOAD Hausarbeit WiSe 2020/21
"""
from django.shortcuts import render
from django.views import View


class PagesView(View):
    """Pages views class"""

    def get_welcome(request):
        """
        displays a welcome page
        :param request: HTTP Request
        :return: renders a page
        """
        return render(request, "welcome.html")
