from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image_url = models.CharField(max_length=2083)
    color=models.CharField(max_length=55)
    brand_name= models.CharField(max_length=55)
    
    def __str__(self):
        return self.name
    