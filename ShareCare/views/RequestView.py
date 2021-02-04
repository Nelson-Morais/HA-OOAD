from django.views import View


class RequestView(View):

    def getIncomingRequests(self, request):
       print('hello')

    def getOutgoingRequest(self, request):
        print()

    def getCreateForm(self, request):
        print()

    def create(self, request):
        print()

    def approved(self, request, id):
        print()