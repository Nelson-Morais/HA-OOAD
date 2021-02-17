"""
Django Request Form

@author Kevin Lucas Simon, Christina Bernhardt ,Nelson Morais
Projekt OOAD Hausarbeit WiSe 2020/21
"""
from django import forms

from apps.bazaar.models import RequestModel


class RequestForm(forms.ModelForm):
    """Describes Request Form"""

    class Meta:
        model = RequestModel
        fields = [
            'text'
        ]
        widgets = {'userowner_id': forms.HiddenInput(),
                   'offer_id': forms.HiddenInput()}
