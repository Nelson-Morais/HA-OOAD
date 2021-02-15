from django import forms

from .models import Offer
from .models import Request


class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = [
            'userowner_id',
            'title',
            'description',
        ]
        widgets = {'userowner_id': forms.HiddenInput()}

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = [
            'text'
        ]
        widgets = {'userowner_id': forms.HiddenInput()}