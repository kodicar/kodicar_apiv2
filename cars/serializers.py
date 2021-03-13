from rest_framework import serializers
from . models import Cars, Photo, Category

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model= Cars
        fields = "__all__"

        # todo for all serializers
        # read_only_fields = ("user", "id", "created", "updated")

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"