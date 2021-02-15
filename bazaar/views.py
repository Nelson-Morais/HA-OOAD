from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import View
from .forms import OfferForm
from .forms import RequestForm
from .models import RequestModel, OfferModel


# displays a list of new offers of the plattform
def get_offer_list(request, latitude=0, longitude=0):
    offer = OfferModel.objects.filter(is_deleted=False)
    context = {
        'offer': offer
    }
    return render(request, "offerlist.html", context)


# displays details of specific offer
@login_required(login_url='login')
def get_offer(request, offer_id):
    return render(request, "offersingle.html", {"offer_id": offer_id, "testvar": offer_id})


# displays offer creation form
@login_required(login_url='login')
def get_offer_creator(request):
    form = OfferForm(request.POST or None)
    if form.is_valid():
        offer = form.save(commit=False)
        offer.userowner_id = request.user.id
        offer.save()
        # reload form, delete if want to redirect:
        form = OfferForm()
    context = {
        'form': form
    }
    return render(request, "create_offer.html", context)


# displays a list of the users offers
@login_required(login_url='login')
def get_personal_offer_list(request):
    return render(request, "requests.html", {"numbers": range(5)})


# displays a list of the users requests to other offers
@login_required(login_url='login')
def get_personal_request_list(request):
    global req
    offer = OfferModel.objects.filter(userowner_id=request.user.id)
    for x in offer:
        req = RequestModel.objects.filter(offer_id=x.offer_id)

    context = {
        'offer': offer,
        'req': req
    }

    return render(request, "requests.html", context)


# saves data from request creation form (offer details view)
@login_required(login_url='login')
def get_request_creator(request, offer_id):
    form = RequestForm(request.POST or None)
    if form.is_valid():
        req = form.save(commit=False)
        req.userowner_id = request.user.id
        req.offer_id = offer_id
        req.save()
    context = {
        'form': form,
        # 'testvar': offer_id
    }
    return render(request, "create_request.html", context)


