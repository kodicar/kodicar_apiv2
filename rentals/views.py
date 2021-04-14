from django.shortcuts import render
from rest_framework import generics 
from rest_framework.views import APIView 
from . models import Rentals 
from . serializers import RentalSerializer
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

# Create your views here.

class RentalList(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Rentals.objects.all()
    serializer_class = RentalSerializer
