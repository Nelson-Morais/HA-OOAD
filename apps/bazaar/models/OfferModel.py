"""
OfferModel represents the DB data of an Offer
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