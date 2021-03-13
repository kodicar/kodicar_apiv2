from django.shortcuts import render
from . models import Contact
from . serializers import ContactSerializer
from rest_framework import generics 

# Create your views here.

class ContactView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    