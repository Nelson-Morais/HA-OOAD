from django.views import View


class OfferView(View):

    def getOffers(request, latitude, longitude):
       print('hello')

    def getPersonalOffers(request):
        print()

    def getCreateForm(request):
        print()

    def create(request):
        print()