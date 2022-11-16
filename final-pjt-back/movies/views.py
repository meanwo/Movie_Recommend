from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Movie, Genre
from .serializers import MovieListSerializer, GenreListSerializer, MovieSerializer, MovietitleSerializer, MovieListSerializer, GenreSerializer

# Create your views here.

@api_view(['GET'])
def genre_list(request):
    genres = get_list_or_404(Genre)
    serializer = GenreListSerializer(genres, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def genre_detail(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    serializer = GenreSerializer(genre)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data, status=status.HTTP_200_OK)