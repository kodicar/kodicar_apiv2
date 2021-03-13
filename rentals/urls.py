from django.urls import path 
from .views import RentalList

urlpatterns = [
    path("rentals/", RentalList.as_view(), name="rentals"),
    
]
