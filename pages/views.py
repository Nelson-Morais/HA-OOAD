from django.shortcuts import render
from django.views import View


# Create your views here.

class MessageView(View):
    def getMessages(self, request):
        return

    def addMessage(self, request, user_id, message):
        return


class OfferView(View):
    def getOffers(self, request, latitude, longitude):
        return

    def getPersonalOffers(self, request):
        return

    def getCreateForm(self, request):
        return

    def create(self, request):
        return


class RequestView(View):
    def getIncomingRequests(self, request):
       return

    def getOutgoingRequest(self, request):
        return

    def getCreateForm(self, request):
        return

    def create(self, request):
        return

    def approved(self, request, id):
        return


class UtilView(View):
    def getWelcome(self, request):
       return




#templates
def index(response):
    return render(response, "index.html")
def offerlist(response):
    return render(response, "offerlist.html", {"numbers": range(100)})
def offersingle(response):
    return render(response, "offersingle.html")
def requests(response):
    return render(response, "requests.html", {"numbers": range(5)})
def messages(response):
    return render(response, "messages.html")

