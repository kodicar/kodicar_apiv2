from django.shortcuts import render
from rest_framework import generics 
from . models import Reviews
from . serializers import ReviewSerializer

# Create your views here.

class ReviewsList(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer

    