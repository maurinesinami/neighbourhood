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
        return self.name_of_neighbourhood
class Profile(models.Model):
    profile_photo= models.ImageField(upload_to = 'dp/')
    location= models.CharField(max_length=50)
    neighbourhood_name=models.ForeignKey(Community,on_delete=models.CASCADE, null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    def __str__(self):
        return self.neighbourhood_name

class Post(models.Model):
    img = models.ImageField(upload_to = 'posts/' ,null=True)
    text= models.CharField(max_length=50)
    profile = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    neighbourhood=models.ForeignKey(Community,on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.img
class Business(models.Model):
    bn_name = models.CharField(max_length=64, unique= True)
    bn_user = models.ForeignKey(User,on_delete=models.CASCADE)
    bn_community = models.ForeignKey(Community, null=True)
    bn_email = models.EmailField(max_length=64, unique= True) 
    def __str__(self):
        return self.bn_name  