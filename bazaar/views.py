from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.views import View
from django.db.models import Q

from notifications.views import add_notification
from .forms import OfferForm
from .forms import RequestForm
from .models import RequestModel, OfferModel


# displays a list of new offers of the plattform
def get_offer_list(request, latitude=0, longitude=0):
    offers = OfferModel.objects.filter(is_deleted=False).order_by('-created_at')
    context = {
        'offers': offers
    }
    return render(request, "offerlist.html", context)


# displays details of specific offer
@login_required(login_url='login')
def get_offer(request, offer_id):
    offer = OfferModel.objects.get(id=offer_id)
    context = {
        'offer': offer
    }
    return render(request, "offersingle.html", context)


# displays offer creation form
@login_required(login_url='login')
def get_offer_creator(request):
    form = OfferForm(request.POST or None)
    if form.is_valid():
        offer = form.save(commit=False)
        offer.userowner_id = request.user.id
        offer.save()
        add_notification(request.user.id, "Neues Angebot", offer.title)
        return redirect('offer_list')
    context = {
        'form': form
    }
    return render(request, "create_offer.html", context)


# displays a list of the users offers
@login_required(login_url='login')
def get_personal_offer_list(request):
    offers = OfferModel.objects.filter(userowner_id=request.user.id)
    context = {
        'offers': offers
    }
    return render(request, "requests.html", context)


# displays a list of the users requests to othS er offers
@login_required(login_url='login')
def get_personal_request_list(request):
    global reqs
    templist = []
    offers = OfferModel.objects.filter(userowner_id=request.user.id)
    for x in offers:
        reqs = RequestModel.objects.filter(~Q(status=3), offer_id=x.id)
        tempdict = {'offer': x,
                    'reqs': reqs}
        templist.append(tempdict)
    context = {
        'offerlist': templist
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
        'offer_id': offer_id
    }
    return render(request, "create_request.html", context)


def request_accept(request, offer_id, request_id):
    requests = RequestModel.objects.filter(offer_id=offer_id)

    for x in requests:
        if x.id == request_id:
            x.status = 2
        else:
            x.status = 3
    requests.save()

    return render(request, "page_yo", {})


def delete_offer(request, offer_id):
    offer = OfferModel.objects.filter(offer_id)
    offer.is_deleted = True
    offer.save()

    return render(request, "page_yo", {})
