from django.shortcuts import render
from rest_framework import generics 
from . models import Reviews
from . serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

# Create your views here.

class ReviewsList(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer

    