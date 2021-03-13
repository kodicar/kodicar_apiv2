from django.db import models
from django.contrib.auth.models import User
from cars.models import Cars
from kodicarapiv2 import settings

# Create your models here.

class Reviews(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    rating = models.IntegerField()
    title = models.CharField( max_length=50)
    body = models.TextField(max_length=500)
    created_at = models.DateTimeField( auto_now=True)

    class Meta:
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return self.title
    

    

    