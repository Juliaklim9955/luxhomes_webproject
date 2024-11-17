from django.db import models

# Create your models here.
class Team(models.Model):
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    role = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    fb_link = models.URLField(max_length=250)
    x_link = models.URLField(max_length=250)
    google_link = models.URLField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True)
    
    #anytime we create a function inside a class we past "self":
    def __str__(self):
        return self.firstname




