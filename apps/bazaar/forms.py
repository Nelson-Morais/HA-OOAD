from django import forms

from .models import OfferModel
from .models import RequestModel


class OfferForm(forms.ModelForm):
    class Meta:
        model = OfferModel
        fields = [
            'userowner_id',
            'title',
            'description',
        ]
        widgets = {'userowner_id': forms.HiddenInput()}

class RequestForm(forms.ModelForm):
    class Meta:
        model = RequestModel
        fields = [
            'text'
        ]
        widgets = {'userowner_id': forms.HiddenInput(),
                   'offer_id': forms.HiddenInput()}
