from django.db import models


class OfferModel(models.Model):
    userowner_id = models.IntegerField(default=0)
    title = models.CharField(max_length=512)
    description = models.CharField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)


class RequestModel(models.Model):
    userowner_id = models.IntegerField()
    offer_id = models.IntegerField(default=0)
    text = models.CharField(max_length=512)
    RequestStatus = (
        ('1', 'open'),
        ('2', 'accepted'),
        ('3', 'declined')
    )
    status = models.CharField(max_length=1, choices=RequestStatus, default=1)
