
from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from kodicarapiv2 import settings
# from django_countries.fields import CountryField
# from users.models import CarRentalCompany, CarOwner





# Create your models here.
class TimeStampedModel(models.Model):
    """ Time Stamped Model"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class AbstractItem(TimeStampedModel):
    """Abstract Item"""

    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True





class Category(models.Model):
    categories = (
        ('Car', 'Car'),
        ('classics', 'classics'),
        ('convertibles', 'convertibles'),
        ('Exotic & Luxury', 'Exotic & Luxury'),
        ('Minivans', 'Minivans'),
        ('Sports', 'Sports'),
        ('SUV', 'SUV'),
        ('Trucks', 'Trucks'),
        ('Vans', 'Vans')
    )
    cat_name = models.CharField(max_length=100, choices=categories, default='Car')
    cat_image = models.ImageField(upload_to = 'categories')

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.cat_name

class Cars(models.Model):
    countries = (
        ('Kenya', 'Kenya'),
        ('Tanzania', 'Tanzania'),
        ('Uganda',  'Uganda'),
        ('Sudan', 'Sudan'),
        ('Somalia', 'Somalia'),
    )

    counties = (


        ('Mombasa','Mombasa'),
        ('Kwale','Kwale'),
        ('Kilifi','Kilifi'),
        ('Tana River','Tana River'),
        ('Lamu','Lamu'),
        ('Taita-Taveta', 'Taita-Taveta'),
        ('Garissa','Garissa'),
        ('Wajir','Wajir'),
        ('Mandera','Mandera'),
        ('Marsabit', 'Marsabit'),
        ('Isiolo', 'Isiolo'),
        ('Meru', 'Meru'),
        ('Tharaka-Nithi', 'Tharaka-Nithi'),
        ('Embu', 'Embu'),
        ('Kitui','Kitui'),
        ('Machakos', 'Machakos'),
        ('Makueni', 'Makueni'),
        ('Nyandarua', 'Nyandarua'),
        ('Nyeri', 'Nyeri'),
        ('Kirinyaga', 'Kirinyaga'),
        ('Murang', 'Murang'),
        ('Kiambu', 'Kiambu'),
        ('Turkana', 'Turkana'),
        ('West Pokot', 'West Pokot'),
        ('Samburu', 'Samburu'),
        ('Trans Nzoia','Trans Nzoia'),
        ('Uasin Gishu', 'Uasin Gishu'),
        ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'),
        ('Nandi','Nandi'),
        ('Baringo', 'Baringo'),
        ('Laikipia', 'Laikipia'),
        ('Nakuru', 'Nakuru'),
        ('Narok', 'Narok'),
        ('Kajiado', 'Kajiado'),
        ('Kericho', 'Kericho'),
        ('Bomet', 'Bomet'),
        ('Kakamega','Kakamega'),
        ('Vihiga', 'Vihiga'),
        ('Bungoma', 'Bungoma'),
        ('Busia', 'Busia'),
        ('Siaya', 'Siaya'),
        ('Kisumu', 'Kisumu'),
        ('Homa Bay','Homa Bay'),
        ('Migori', 'Migori'),
        ('Kisii', 'Kisii'),
        ('Nyamira', 'Nyamira'),
        ('Nairobi', 'Nairobi'),
    )

    makes = (
        ('Tesla', 'Tesla'),
        ('Lamborghini', 'Lamborghini'),
        ('Jeep', 'Jeep'),
        ('Rolls Royce', 'Rolls Royce'),
        ('Mercedes Benz', 'Mercedes Benz'),
        ('Ferrari', 'Ferrari'),
        ('Maserati', 'Maserati'),
        ('Porsche', 'Porsche'),
        ('BMW', 'Subaru'),
        ('Acura', 'Acura'),
    )

    profiles = (
        ('CAR_OWNER', 'Car_owner'),
        ('CAR_RENTAL_COMPANY', 'Car_Rental_Company'),
    )
    # location
    
    country = models.CharField(default='select country', max_length=100 , choices=countries)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    county = models.CharField(max_length=200, choices=counties, default='Nairobi')
    postal_code = models.CharField(max_length=100)

    # car information
    year = models.IntegerField()
    make = models.CharField(max_length=100, default='Tesla', choices=makes)
    model = models.CharField(max_length=100)
    odometer = models.CharField(max_length=300)
    car_category = models.ForeignKey(Category, on_delete= models.CASCADE)
    colour = models.CharField(max_length=50)
    mpg = models.CharField(max_length=50)
    seats = models.IntegerField()
    doors = models.IntegerField()

    Transmissions= (
        ('Automatic', 'Automatic'),
        ('Manual', 'Manual'),
    )
    transmission = models.CharField(max_length=200, choices=Transmissions)
    market_value = models.CharField(max_length=300)
    vin = models.CharField(max_length=17)
    license_plate = models.CharField(max_length=30)

    # car_image = models.ImageField( upload_to='cars')
    price_per_day = models.IntegerField()
    car_details = models.TextField()
    description = models.TextField()
    # car availability 
    as_from = models.DateField()
    to = models.DateField()
    guideline = models.TextField(max_length=300)
    safety_and_quality_standards = models.BooleanField()

    # features 
    # cretae single textfields to handle description
    usb_charger = models.BooleanField(default=False)
    gps = models.BooleanField()
    automatic = models.BooleanField()
    sunroof = models.BooleanField()
    apple_car_play = models.BooleanField()
    all_wheel_drive = models.BooleanField()
    bluetooth = models.BooleanField()
    audio_input = models.BooleanField()
    convertible = models.BooleanField()
    child_seat = models.BooleanField()
    longterm_car = models.BooleanField()
    bike_rack = models.BooleanField()


    # owner information
    profile_photo = models.ImageField( upload_to = 'profiles')
    mobile_number = models.IntegerField()
    drivers_license = models.CharField(max_length=200)
    your_goals = models.TextField()
    date_added = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.make} - {self.model} - {self.year}'

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0 
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rating_average()
            return round(all_ratings / len(all_reviews), 2)
        return 0

    def first_photo(self):
        try: 
            photo = self.photos.first()
            return photo.file.url 
        except Exception:
            return None

    def get_next_four(self):
        photos = self.photos.all()[1:5]
        return photos
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        self.city = str.title(self.city)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Cars"
        ordering = ['-pk']


class Photo(TimeStampedModel):
    """Photo Model Definition"""
    # car = models.ForeignKey("Car.Model", verbose_name=_(""), on_delete=models.CASCADE)
    # phot= models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)


    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to = 'car_photos')
    cars = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name="photos")

    def __str__(self):
        return self.caption

    # todo 
    # def __str__(self):
    #     return self.car.name
    

    



