"""
Django bazaar Forms

@author Kevin Lucas Simon, Christina Bernhardt ,Nelson Morais
Projekt OOAD Hausarbeit WiSe 2020/21
"""
from django import forms
from .models import OfferModel
from .models import RequestModel


class OfferForm(forms.ModelForm):
    """Describes Offer Form"""

    class Meta:
        model = OfferModel
        fields = [
            'userowner_id',
            'title',
            'description',
        ]
        widgets = {'userowner_id': forms.HiddenInput()}


class RequestForm(forms.ModelForm):
    """Describes Request Form"""

    class Meta:
        model = RequestModel
        fields = [
            'text'
        ]
        widgets = {'userowner_id': forms.HiddenInput(),
                   'offer_id': forms.HiddenInput()}
