from django.urls import path 
from .views import UserCreate, LoginView, UserDetail


urlpatterns = [
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
    path("user_detail/<int: pk>/", UserDetail.as_view(), name="user_detail"),
    
    
]