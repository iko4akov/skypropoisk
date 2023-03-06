from .genres import api as genre_ns
from .directors import api as director_ns
from .movies import api as movie_ns
from .like_movie import api as like_movie_ns

__all__ = [
    'genre_ns',
    'director_ns',
    'movie_ns',
    'like_movie_ns'
]
