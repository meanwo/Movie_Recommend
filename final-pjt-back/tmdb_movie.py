import requests
import json
from pprint import pprint

TMDB_API_KEY = 'd43c34da8b6513938295a31cd66258b2'

def get_movie_datas():
    total_data = []

    # 1페이지부터 500페이지까지 (페이지당 20개, 총 10,000개)
    for i in range(1, 100):
        request_url = "https://api.themoviedb.org/3/movie/popular"
        params = {
            "api_key" : TMDB_API_KEY,
            "language" : "ko-KR",
            "page" : i,
        }
        # request_url = f"<https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}>"
        movies = requests.get(request_url, params=params).json()
        pprint(movies)
        for movie in movies['results']:
            if movie.get('release_date', ''):
                fields = {
                    # 'movie_id': movie['id'],
                    'title': movie['title'],
                    'released_date': movie['release_date'],
                    # 'popularity': movie['popularity'],
                    'vote_avg': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'genres': movie['genre_ids']
                }

                data = {
                    "pk": movie['id'],
                    "model": "movies.movie",
                    "fields": fields
                }

                total_data.append(data)

    with open("movie_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=4, ensure_ascii=False)

get_movie_datas()



def get_genre_datas():
    #1. URL 정보 설정
    request_url_2 = "https://api.themoviedb.org/3/genre/movie/list"
    params = {
        'api_key' : TMDB_API_KEY,
        "language" : "ko-KR",
    }
    total_data = []
    # 2. 요청 및 응답
    genres = requests.get(request_url_2, params=params).json()
    genres = genres['genres']
    pprint(genres)


    for genre in genres:
        
        fields = {
            
            # 'id': genre['id'],
            'name': genre['name'],
        }

        data = {
            "pk": genre['id'],
            "model": "movies.genre",
            "fields": fields
        }

        total_data.append(data)

    with open("genre_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=4, ensure_ascii=False)

get_genre_datas()

