"""
Django bazaar Models
@author Kevin Lucas Simon, Christina Bernhardt ,Nelson Morais
Projekt OOAD Hausarbeit WiSe 2020/21
"""
from django.db import models


class Message(models.Model):
    """describes the Message model"""
    user_owner_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=64)
    content = models.CharField(max_length=512)