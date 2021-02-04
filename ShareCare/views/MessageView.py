from django.views import View


class MessageView(View):

    def getMessages(self, request):
       print('hello')

    def addMessage(self, id, message):
        print()