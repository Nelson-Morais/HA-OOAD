"""
Django bazaar Models
@author Kevin Lucas Simon, Christina Bernhardt ,Nelson Morais
Projekt OOAD Hausarbeit WiSe 2020/21
"""
from django.db import models


class OfferModel(models.Model):
    """Describes Offer Model"""
    userowner_id = models.IntegerField(default=0)
    title = models.CharField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=512)
    is_closed = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)


class RequestModel(models.Model):
    """Describes Request Model"""
    userowner_id = models.IntegerField()
    offer_id = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=512)
    RequestStatus = (
        (1, 'open'),
        (2, 'accepted'),
        (3, 'declined')
    )
    status = models.IntegerField(choices=RequestStatus, default=1)
    is_deleted = models.BooleanField(default=False)
