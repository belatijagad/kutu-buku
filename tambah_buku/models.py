from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255, name="Title")
    category = models.CharField(max_length=100, name="Category")
    image = models.URLField(name="Image")
    rating = models.IntegerField(name="Rating")
    description = models.TextField(null=True, blank=True, name="Description")

class Ulasan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)