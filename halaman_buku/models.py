from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    sha256sum = models.CharField(max_length=64, unique=True, null=True, blank=True)
    title = models.TextField()
    author = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    chapters = models.IntegerField()
    img_src = models.TextField()
    genre = models.TextField(blank=True)
    synopsis = models.TextField()
    reviewers = models.IntegerField()
    score = models.FloatField()
    published_at = models.DateField(auto_now_add=True)

class Ulasan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField(null=True, blank=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)