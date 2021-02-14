from django.shortcuts import render
from django.views import View


class PageView(View):
    # displays a welcome page
    def get_welcome(self):
        return render(self, "welcome.html")
