from django.shortcuts import render
from rest_framework import generics
from . models import Article, Comments
from . serializers import ArticleSerializer, CommentsSerializer
from rest_framework import viewsets

# Create your views here.
# preferring to use generic api views as compared to viewsets, but will use viewsets if need be 
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(generics.RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class CommentsList(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer




