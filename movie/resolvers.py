import json
import os

MOVIES_PATH = os.path.join(os.path.dirname(__file__), 'data', 'movies.json')
ACTORS_PATH = os.path.join(os.path.dirname(__file__), 'data', 'actors.json')

def movie_with_id(_, info, _id):
    with open(MOVIES_PATH, 'r') as f:
        movies = json.load(f)
        for movie in movies['movies']:
            if movie['id'] == _id:
                return movie
    return None

def update_movie_rate(_, info, _id, _rate):
    newmovies = {}
    newmovie = {}
    with open(MOVIES_PATH, 'r') as f:
        movies = json.load(f)
        for movie in movies['movies']:
            if movie['id'] == _id:
                movie['rating'] = _rate
                newmovie = movie
                newmovies = movies
                with open(MOVIES_PATH, 'w') as f:
                    json.dump(newmovies, f)
    return newmovie

def resolve_actors_in_movie(movie, info):
    with open(ACTORS_PATH, 'r') as f:
        actors = json.load(f)
        result = [actor for actor in actors['actors'] if movie['id'] in actor['films']]
        return result