from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import View
from .forms import OfferForm
from .forms import RequestForm

# displays a list of new offers of the plattform
def get_offer_list(request, latitude=0, longitude=0):
    return render(request, "offerlist.html", {"numbers": range(100)})


# displays details of specific offer
@login_required(login_url='login')
def get_offer(request, offer_id=0):
    return render(request, "offersingle.html", {"offer_id": offer_id, "testvar": offer_id})


# displays offer creation form
@login_required(login_url='login')
def get_offer_creator(request):
    form = OfferForm(request.POST or None)
    if form.is_valid():
        offer = form.save(commit=False)
        offer.userowner_id = request.user.id
        offer.save()
        #reload form, delete if want to redirect:
        form = OfferForm()
    context = {
        'form': form
    }
    return render(request, "create_offer.html", context)


# saves data from offer creation form: NOT NEEDED ?
# @login_required(login_url='login')
# def save_offer_creator(self, request):
##   return render(self, "placeholder.html")

# displays a list of the users offers
@login_required(login_url='login')
def get_personal_offer_list(request):
    return render(request, "requests.html", {"numbers": range(5)})


# displays a list of the users requests to other offers
@login_required(login_url='login')
def get_personal_request_list(request):
    return render(request, "requests.html", {"numbers": range(5)})


# saves data from request creation form (offer details view)
@login_required(login_url='login')
def get_request_creator(request):
    form = RequestForm(request.POST or None)
    if form.is_valid():
        req = form.save(commit=False)
        req.userowner_id = request.user.id
        req.save()
    context = {
        'form': form,
        #'testvar': offer_id
    }
    return render(request, "create_request.html", context)


# approves specific request for users offer
@login_required(login_url='login')
def approve_incoming_request(request, offer_id):
    return render(request, "placeholder.html", {"testvar": offer_id})
