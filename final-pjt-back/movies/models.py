from django.db import models
from django.conf import settings

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    released_date = models.DateField()
    vote_avg = models.FloatField() # 평점 IntegerField에서 FloatField로 변경하기!
    overview = models.TextField()
    poster_path = models.TextField()
    genres = models.ManyToManyField(Genre, related_name='movies')
    recommend = models.JSONField(null=True, blank=True)

class Comment(models.Model):
    spoiler = models.BooleanField(default=False)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

