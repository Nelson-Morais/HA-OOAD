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
    return render(request, "offer_list.html", context)


# displays details of specific offer
@login_required(login_url='login')
def get_offer(request, offer_id):
    offer = OfferModel.objects.get(id=offer_id)
    context = {
        'offer': offer
    }
    return render(request, "offer_single.html", context)


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


# displays a list of the users requests to othS er offers
@login_required(login_url='login')
def get_personal_offer_list(request):
    object_list = []
    offers = OfferModel.objects.filter(userowner_id=request.user.id)
    for offer in offers:
        requests = RequestModel.objects.filter(~Q(status=3), offer_id=offer.id)
        object_tuple = {'offer': offer,
                        'requests': requests}
        object_list.append(object_tuple)
    context = {
        'objects': object_list
    }
    return render(request, "my_offer_list.html", context)


# displays a list of the users requests to othS er offers
@login_required(login_url='login')
def get_personal_request_list(request):
    object_list = []
    requests = RequestModel.objects.filter(userowner_id=request.user.id)
    for req in requests:
        offer = OfferModel.objects.get(id=req.offer_id)
        object_tuple = {'request': req,
                        'offer': offer}
        object_list.append(object_tuple)
    context = {
        'objects': object_list
    }
    return render(request, "my_request_list.html", context)


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
