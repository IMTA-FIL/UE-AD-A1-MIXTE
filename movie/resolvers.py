from graphql import GraphQLError
from utils import write_movies, load_actors, load_movies

def movie_with_id(_, info, _id):
    movies = load_movies()
    for movie in movies:
        if movie["id"] == _id:
            return movie

def update_movie_rate(_, info, _id, _rate):
    new_movies = {}
    new_movie = {}
    movies = load_movies()
    
    for movie in movies:
        if movie['id'] == _id:
            movie['rating'] = _rate
            new_movie = movie
            new_movies = movies
    
    write_movies(new_movies)
    return new_movie

def add_movie(_, info, _id, _title, _rate, _director):
    new_movies = {}
    movies = load_movies()
    
    for movie in movies:
        if movie['id'] == _id:
            raise GraphQLError(f"movie with {_id} already exists")

    new_movies = movies
    new_movie = {
        "id": _id,
        "title": _title,
        "rating": _rate,
        "director": _director
    }
    new_movies.append(new_movie)
    
    write_movies(new_movies)
    return new_movie

def resolve_actors_in_movie(movie, info):
    actors = load_actors()
    result = [actor for actor in actors if movie['id'] in actor['films']]
    return result