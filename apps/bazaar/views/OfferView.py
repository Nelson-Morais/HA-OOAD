"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.


OfferView controls activity belonging to offers

@author Kevin Lucas Simon, Christina Bernhardt ,Nelson Morais
Projekt OOAD Hausarbeit WiSe 2020/21
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views import View

from apps.bazaar.adapters.notifications_adapter import add_notification
from apps.bazaar.forms import OfferForm
from apps.bazaar.models import OfferModel, RequestModel


class OfferView(View):
    """Offer views class"""

    @login_required(login_url='login')
    def create_offer(request):
        """
        displays offer creation form
        :return: renders a page and sends a dictionary to the view
        """
        form = OfferForm(request.POST or None)

        if form.is_valid():
            offer = form.save(commit=False)
            offer.userowner_id = request.user.id
            offer.save()

            add_notification(request.user.id, "Angebot platziert", offer.title)
            return redirect('offer_list')

        return render(request, "create_offer.html", {
            'form': form
        })

    @login_required(login_url='login')
    def delete_offer(request, offer_id):
        """
        deletes the offer
        :param offer_id: ID of the offer to be deleted
        :return: redirects to a page
        """
        offer = OfferModel.objects.filter(is_deleted=False).get(id=offer_id)
        offer.is_deleted = True
        offer.save()

        requests = RequestModel.objects.filter(is_deleted=False).filter(offer_id=offer_id)
        for req in requests:
            req.is_deleted = True
            req.save()
            add_notification(req.userowner_id, "Angebot ihrer Anfrage gelöscht", offer.title)

        add_notification(request.user.id, "Angebot gelöscht", offer.title)
        return redirect('personal_offer_list')

    @login_required(login_url='login')
    def get_offer(request, offer_id):
        """
        displays details of specific offer
        :param offer_id: ID of the offer to get from the Database
        :return: renders a page and sends a dictionary to the view
        """
        offer = OfferModel.objects.filter(is_deleted=False).get(id=offer_id)
        return render(request, "offer_single.html", {
            'offer': offer
        })

    def offers_listing(request):
        """
        displays a list of new offers of the plattform
        :return: renders a page and sends a dictionary to the view
        """
        offers = OfferModel.objects.filter(is_deleted=False).order_by('-created_at')
        return render(request, "offer_list.html", {
            'offers': offers
        })

    @login_required(login_url='login')
    def personal_offers_listing(request):
        """
        displays a list of the users requests to other offers
        :return: renders a page and sends a dictionary to the view
        """
        object_list = []
        offers = OfferModel.objects.filter(is_deleted=False).filter(userowner_id=request.user.id).order_by(
            '-created_at')

        for offer in offers:
            requests = RequestModel.objects.filter(is_deleted=False).filter(offer_id=offer.id).order_by('-created_at')
            object_list.append({
                'offer': offer,
                'requests': requests,
            })

        return render(request, "my_offer_list.html", {
            'objects': object_list
        })
