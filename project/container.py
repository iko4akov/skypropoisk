from project.dao import GenresDAO, DirectorsDAO, UsersDAO, MoviesDAO, LikeMovieDao

from project.services import GenresService, DirectorsService, UserService, MovieService, AuthService, LikeMovieService
from project.setup.db import db

# DAO
genre_dao = GenresDAO(db.session)
director_dao = DirectorsDAO(db.session)
user_dao = UsersDAO(db.session)
movie_dao = MoviesDAO(db.session)
like_movie_dao = LikeMovieDao(db.session)


# Services
genre_service = GenresService(dao=genre_dao)
director_service = DirectorsService(dao=director_dao)
user_service = UserService(dao=user_dao)
movie_service = MovieService(dao=movie_dao)
auth_service = AuthService(user_service)
like_movie_service = LikeMovieService(dao=like_movie_dao)

