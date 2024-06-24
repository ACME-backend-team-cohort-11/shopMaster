""" Defines product model for the application. """
from django.db import models

class Product(models.Model):
    """ Defines product model. """
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stars = models.IntegerField()
    image_url = models.ImageField(upload_to='products/')


    def __str__(self):
        """ Returns product name. """
        return self.name
