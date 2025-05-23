from django.db import models
from cars.models import Cars
from django.contrib.auth.models import User
from kodicarapiv2 import settings

# Create your models here.

class Rentals(models.Model):
    renter = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    start_date = models.DateField( auto_now=False)
    end_date = models.DateField( auto_now=False)
    status = models.CharField( max_length=50)

    class Meta:
        verbose_name_plural = 'My Rentals'

