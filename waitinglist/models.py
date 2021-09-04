from django.db import models

# Create your models here.

class WaitingList(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name_plural = 'WaitingList'
