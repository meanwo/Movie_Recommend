from rest_framework import serializers
from .models import Movie, Genre, Comment

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
        fields = ('id', 'title', 'released_date', 'vote_avg', 'overview', 'poster_path', 'genres', 'recommend')

class GenreListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = ('id', 'name',)

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('movie', 'user', 'username')

class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)

    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'overview', 'released_date', 'poster_path', 'genres', 'vote_avg', 'comment_set', 'comment_count', 'recommend',)







