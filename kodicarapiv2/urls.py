"""kodicarapiv2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', include("cars.urls")),
    path('blog/', include("blog.urls")),
    path('contact/', include("contact.urls")),
    path('users/', include("users.urls")),
    path('reviews/', include("reviews.urls")),
    path('rentals/', include("rentals.urls")),
    path('auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('waitinglist/', include('waitinglist.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                            document_root=settings.MEDIA_ROOT
    )
