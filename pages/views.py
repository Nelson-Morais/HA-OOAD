from django.shortcuts import render


# displays a welcome page
def get_welcome(request):
    return render(request, "welcome.html")
