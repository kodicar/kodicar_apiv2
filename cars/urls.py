from django.urls import path 
from .views import CarList, CarDetail,PhotoList, CarDelete, CategoryList, CarCreate

urlpatterns = [
    path("cars/", CarList.as_view(), name="cars_list"),
    path("cars/<int:pk>/", CarDetail.as_view(), name="car_detail"),
    path("car/<int:pk>/", CarDelete.as_view(), name="car_delete"),
    path("photos/", PhotoList.as_view(), name="photos_list"),
    path("categories/", CategoryList.as_view(), name="category_list"), 
    path("carcreate/", CarCreate.as_view(), name="car_create"),
    
    
]