from django.shortcuts import render
from rest_framework import generics 
from rest_framework.views import APIView 
from . models import Rentals 
from . serializers import RentalSerializer

# Create your views here.

class RentalList(generics.ListCreateAPIView):
    queryset = Rentals.objects.all()
    serializer_class = RentalSerializer
