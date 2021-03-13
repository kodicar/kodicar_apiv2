from django.urls import path 
from .views import ArticleList, ArticleDetail, CommentsList, ArticleViewSet
from rest_framework.routers import DefaultRouter


# router = DefaultRouter
# router.register('articles', ArticleViewSet, viewset="articles")

urlpatterns = [
    path("articles/", ArticleList.as_view()),
    path("articles/<int:pk>/", ArticleDetail.as_view()),
    path("comments/", CommentsList.as_view()),
    
]

# urlpatterns += router.urls
