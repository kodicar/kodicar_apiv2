from django.db import models

# Create your models here.

class Contact(models.Model):
    fname = models.CharField( max_length=50)
    lname = models.CharField( max_length=50)
    email = models.EmailField( max_length=254, unique = True)
    subject = models.CharField( max_length=300)
    message = models.TextField(max_length = 3000)
    date_sent = models.DateTimeField( auto_now=True)

    class Meta:
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.email
    