from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    released_date = models.DateField()
    vote_avg = models.IntegerField()
    overview = models.TextField()
    poster_path = models.TextField()
    genres = models.ManyToManyField(Genre, related_name='movies')
