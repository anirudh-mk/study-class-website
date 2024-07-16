from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    price_drop = models.BooleanField()
    image = models.ImageField(upload_to='media')


class Sales(models.Model):
    name = models.CharField(max_length=200),
    is_avilable = models.BooleanField(default=True)