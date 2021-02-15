from django.db import models

# Create your models here.
class Offer(models.Model):
    userowner_id = models.IntegerField(default=0)
    title = models.CharField(max_length=512)
    description = models.CharField(max_length=512)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    #DateTime field?
    pickup_starttime = models.CharField(max_length=8)
    pickup_endtime = models.CharField(max_length=8)
    is_deleted = models.BooleanField(default=False)

