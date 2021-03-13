from django.contrib import admin
from . models import Cars, Photo, Category

# Register your models here.
admin.site.register(Category)
admin.site.register(Cars)
admin.site.register(Photo)

