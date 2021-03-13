from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=300)
    short_description = models.CharField(max_length=500)
    content = models.TextField(max_length=5000)
    article_image = models.ImageField(upload_to= 'articles')
    creator = models.ForeignKey(User,  on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title

class Comments(models.Model):
    """ customers to comment on each blog """
    # this will help get customer feedback 
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Comments'
    def __str__(self):
        return self.comment
    
    
