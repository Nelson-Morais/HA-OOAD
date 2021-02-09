from django.db import models

# Create your models here.
class Message(models.Model):
    userowner_id = models.IntegerField()
    created_at = models.DateField()
    #Length content ? parameter: CharField(max_length = 50) zB
    content = models.CharField(max_length=512)
    #default wert für boolean ? True False? BooleanField(default=True)
    is_read = models.BooleanField()



class Request(models.Model):
    request_id = models.IntegerField()
    userowner_id = models.IntegerField()
    text = models.CharField(max_length=512)

    RequestStatus = (
        ('1','open'),
        ('2','accepted'),
        ('3','deleted')
    )
    status = models.CharField(max_length=512,choices=RequestStatus)



class Offer(models.Model):
    offer_id = models.IntegerField()
    userowner_id = models.IntegerField()
    title = models.CharField(max_length=512)
    description = models.CharField(max_length=512)
    latitude = models.FloatField()
    longitude = models.FloatField()
    #DateTime field?
    pickup_starttime = models.DateTimeField()
    pickup_endtime = models.DateTimeField()
    is_deleted = models.BooleanField(default=False)


class Category(models.Model):
    category_id = models.IntegerField()
    name = models.CharField(max_length=512)



