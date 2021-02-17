"""
Django Offer Form

@author Kevin Lucas Simon, Christina Bernhardt ,Nelson Morais
Projekt OOAD Hausarbeit WiSe 2020/21
"""
from django import forms

from apps.bazaar.models import OfferModel


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
