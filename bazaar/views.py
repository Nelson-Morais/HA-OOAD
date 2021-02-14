from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import View


class OfferView(View):
    # displays a list of new offers of the plattform
    def get_offer_list(self, latitude=0, longitude=0):
        return render(self, "offerlist.html", {"numbers": range(100)})

    # displays details of specific offer
    @login_required(login_url='login')
    def get_offer(self, offer_id=0):
        return render(self, "offersingle.html", {"offer_id": offer_id, "testvar": offer_id})

    # displays offer creation form
    @login_required(login_url='login')
    def get_offer_creator(self):
        return render(self, "placeholder.html")

    # saves data from offer creation form
    @login_required(login_url='login')
    def save_offer_creator(self):
        return

    # displays a list of the users offers
    @login_required(login_url='login')
    def get_personal_offer_list(self):
        return render(self, "requests.html", {"numbers": range(5)})


class RequestView(View):
    # displays a list of the users requests to other offers
    @login_required(login_url='login')
    def get_personal_request_list(self):
        return render(self, "requests.html", {"numbers": range(5)})

    # saves data from request creation form (offer details view)
    @login_required(login_url='login')
    def save_request_creator(self, offer_id):
        return render(self, "placeholder.html", {"testvar": offer_id})

    # approves specific request for users offer
    @login_required(login_url='login')
    def approve_incoming_request(self, offer_id):
        return
