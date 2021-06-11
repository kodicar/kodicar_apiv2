from rest_framework import serializers
from . models import Cars, Photo, Category

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model= Cars
        # fields = ("country", "street_address", "city", "county", "postal_code", "year", 
        #             "make", "model", "odometer", "colour", "mpg", "seats", "doors", "transmission", 
        #             "market_value", "vin", "license_plate", "price_per_day", "car_details", "description", 
        #             "as_from", "to", "guideline", "safety_and_quality_standards", "usb_charger", "gps", 
        #             "automatic", "sunroof", "apple_car_play", "all_wheel_drive", "bluetooth", "audio_input", 
        #             "convertible", "child_seat", "longterm_car", "bike_rack", "profile_photo", "mobile_number", 
        #             "drivers_license", "your_goals", "car_category"
        # )
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