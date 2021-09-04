from django.shortcuts import render
from . models import WaitingList
from . serializers import WaitingListSerializer
from rest_framework import generics

# Create your views here.

class WaitingListView(generics.CreateAPIView):
    queryset = WaitingList.objects.all()
    serializer_class = WaitingListSerializer
