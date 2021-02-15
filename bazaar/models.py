from django.db import models

# Create your models here.
class Offer(models.Model):
    userowner_id = models.IntegerField(default=0)
    title = models.CharField(max_length=512)
    description = models.CharField(max_length=512)
    is_deleted = models.BooleanField(default=False)


class Request(models.Model):

    userowner_id = models.IntegerField()
    text = models.CharField(max_length=512)
    RequestStatus = (
        ('1','open'),
        ('2','accepted'),
        ('3','deleted')
    )
    status = models.CharField(max_length=1,choices=RequestStatus, default=1)
