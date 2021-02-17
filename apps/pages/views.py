"""
Notification Interface for external Apps

@author Kevin Lucas Simon, Nelson Morais, Christina Bernhardt
Projekt OOAD Hausarbeit WiSe 2020/21
"""
from django.shortcuts import render


def get_welcome(request):
    """
    displays a welcome page
    :param request: HTTP Request
    :return: renders a page
    """
    return render(request, "welcome.html")
