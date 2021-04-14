from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Cars, Photo, Category
from .serializers import CarSerializer, PhotoSerializer, CategorySerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from . permissions import *




class CarList(generics.ListAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarSerializer

class CarDetail(generics.RetrieveDestroyAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarSerializer

class CarCreate(generics.CreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Cars.objects.all()
    serializer_class = CarSerializer

    # def get(self, request, format=None):
    #     content = {
    #         'user': unicode(request.user),
    #         'auth': unicode(request.auth),
    #     }

    #     return Response(content)


class CarDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner]
    queryset = Cars.objects.all()
    serializer_class = CarSerializer

class PhotoList(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # def post(self, request, *args, **kwargs):
    #     file = request.data['file']
    #     image = Category.objects.create(cat_image=file)
    #     return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)


    




