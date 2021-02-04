from django.views import View


class UtilView(View):

    def getWelcome(self, request):
       print('hello')
