from django.db import models

class Community(models.Model):
    image = models.ImageField(upload_to = 'jirani/')
    name = models.CharField(max_length=55)
    location = models.CharField(max_length=50)
    created_by = models.CharField(max_length=50)
    health_dpt = models.CharField(max_length=50)
    police_dpt = models.CharField(max_length=50)

    def __str__(self):
        return location



