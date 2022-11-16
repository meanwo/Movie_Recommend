from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie, Genre

# Create your views here.

@api_view()
def get_movie(request):
    movies = Movie.objects.all()
    serializer = 