from project.dao.base import BaseDAO
from project.models import Genre, Director, User, Movie, LikeMovie


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre

class DirectorsDAO(BaseDAO[Director]):
    __model__ = Director

class MoviesDAO(BaseDAO[Movie]):
    __model__ = Movie

class UsersDAO(BaseDAO[User]):
    __model__ = User

class LikeMovieDao(BaseDAO[LikeMovie]):
    __model__ = LikeMovie
