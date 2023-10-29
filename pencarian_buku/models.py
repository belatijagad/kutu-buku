from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255, name="Title")
    category = models.CharField(max_length=100, name="Category")
    image = models.URLField(name="Image")
    rating = models.IntegerField(name="Rating")
    description = models.TextField(null=True, blank=True, name="Description")
    upc = models.CharField(max_length=12, unique=True, name="UPC")
    product_type = models.CharField(max_length=50, name="Product Type", default="Books")
    price_excl_tax = models.DecimalField(max_digits=6, decimal_places=2, name="Price (excl")
    price_incl_tax = models.DecimalField(max_digits=6, decimal_places=2, name="Price (incl")
    tax = models.DecimalField(max_digits=6, decimal_places=2, name="Tax")
    availability = models.CharField(max_length=50, name="Availability")
    number_of_reviews = models.IntegerField(name="Number of reviews")