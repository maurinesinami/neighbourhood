from django.db import models
from django.contrib.auth.models import User
class Community(models.Model):
    image = models.ImageField(upload_to = 'jirani/')
    name_of_neighbourhood = models.CharField(max_length=55)
    location = models.CharField(max_length=50)
    created_by = models.CharField(max_length=50)
    health_dpt = models.CharField(max_length=50)
    police_dpt = models.CharField(max_length=50)

    def __str__(self):
        return location
class Profile(models.Model):
    profile_photo= models.ImageField(upload_to = 'dp/')
    location= models.CharField(max_length=50)
    neighbourhood_name=models.CharField(max_length=50)
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)


class Post(models.Model):
    img = models.ImageField(upload_to = 'posts/')
    img_caption = models.CharField(max_length=50)
    profile = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.img
       