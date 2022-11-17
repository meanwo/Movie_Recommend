from rest_framework import serializers
from .models import Movie, Genre

class MovietitleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('title',)
        
class GenreSerializer(serializers.ModelSerializer):
    # movies = MovietitleSerializer(many=True, read_only=True)
    class Meta:
        model = Genre
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ('id', 'title', 'released_date', 'vote_avg', 'overview', 'poster_path', 'genres')

class GenreListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'name',)


class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('id', 'title', 'overview', 'released_date', 'poster_path', 'genres',)




