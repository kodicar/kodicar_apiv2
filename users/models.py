from django.db import models
from django.contrib.auth.models import AbstractUser
from cars.models import Cars
from rentals.models import Rentals
from reviews.models import Reviews

# Create your models here.

class Profile(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    avatar = models.ImageField(upload_to="avatars", blank=True)
    favs = models.ManyToManyField("cars.Cars", related_name="favs")
    rented = models.ManyToManyField("rentals.Rentals", related_name="rentals")
    review = models.ManyToManyField("reviews.Reviews", related_name="review")
    

    def car_count(self):
        return self.cars.count()

    def rentals_count(self):
        return self.rentals.count()

    def reviews_count(self):
        return self.reviews.count()

    def __str__(self):
        return self.username
