"""
RequestView controls activity belonging to requests

@author Kevin Lucas Simon, Christina Bernhardt ,Nelson Morais
Projekt OOAD Hausarbeit WiSe 2020/21
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views import View

from apps.bazaar.adapters.notifications_adapter import add_notification
from apps.bazaar.forms import RequestForm
from apps.bazaar.models import OfferModel, RequestModel


class RequestView(View):
    """Request View Class"""

    @login_required(login_url='login')
    def create_request(request, offer_id):
        """
        saves data from request creation form (offer details view)
        :param offer_id: ID of the offer attached to the request
        :return: renders a page and sends a dictionary to the view
        """
        form = RequestForm(request.POST or None)
        if form.is_valid():
            req = form.save(commit=False)
            req.userowner_id = request.user.id
            req.offer_id = offer_id
            req.save()

            offer = OfferModel.objects.filter(is_deleted=False).get(id=offer_id)
            add_notification(request.user.id, "Anfrage verschickt", req.text)
            add_notification(offer.userowner_id, "Anfrage erhalten!", req.text)
            return redirect('offer_list')

        return render(request, "create_request.html", {
            'form': form,
            'offer_id': offer_id
        })

    @login_required(login_url='login')
    def accept_request(request, offer_id, request_id):
        """
        accepts one request from offer, discards all other requests from offer
        :param offer_id: ID of the offer attached to the requests
        :param request_id: ID of the accepted request
        :return: redirects to a page
        """
        offer = OfferModel.objects.filter(is_deleted=False).get(id=offer_id)
        offer.is_closed = True
        offer.save()

        requests = RequestModel.objects.filter(is_deleted=False).filter(offer_id=offer_id).order_by('-created_at')
        for req in requests:
            if req.id == request_id:
                req.status = 2
                req.save()
                add_notification(req.userowner_id, "Anfrage angenommen!", offer.title)
            else:
                req.status = 3
                req.save()
                add_notification(req.userowner_id, "Anfrage abgelehnt", offer.title)

        return redirect('personal_offer_list')

    @login_required(login_url='login')
    def delete_request(request, request_id):
        """
        deletes the request
        :param request_id: ID of the request to be deleted
        :return: redirects to a page
        """
        req = RequestModel.objects.filter(is_deleted=False).get(id=request_id)
        if req.status == 1:
            req.is_deleted = True
            req.save()
            add_notification(request.user.id, "Anfrage gelöscht", req.text)
            offer = OfferModel.objects.filter(is_deleted=False).get(id=req.offer_id)
            add_notification(offer.userowner_id, "Eingehende Anfrage gelöscht", req.text)

        return redirect('personal_request_list')

    @login_required(login_url='login')
    def personal_request_listing(request):
        """
        displays a list of the users requests to othS er offers
        :return: renders a page and sends a dictionary to the view
        """
        object_list = []
        requests = RequestModel.objects.filter(is_deleted=False).filter(userowner_id=request.user.id).order_by(
            '-created_at')

        for req in requests:
            offer = OfferModel.objects.get(id=req.offer_id)
            if not offer.is_deleted:
                object_list.append({
                    'request': req,
                    'offer': offer,
                })

        return render(request, "my_request_list.html", {
            'objects': object_list
        })
