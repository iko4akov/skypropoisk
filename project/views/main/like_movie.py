from flask import request
from flask_restx import Namespace, Resource
from project.container import like_movie_service
from project.setup.api.models import like_movie
from project.models import LikeMovie
from project.helpers.decorators import auth_required, user_required

api = Namespace('favorite/movies')

@api.route("/")
class LikeMoviesView(Resource):

    @api.marshal_with(like_movie, as_list=True, code=200, description="OK")
    def get(self):
        return like_movie_service.get_all()


@api.route('/<int:movie_id>/')
class LikeMovieView(Resource):

    @api.marshal_with(like_movie, as_list=True, code=200, description="OK")
    @auth_required
    @user_required
    def post(self, movie_id, user) -> LikeMovie:
        """
        Create movie_like
        """

        return like_movie_service.create(movie_id, user)

    @api.marshal_with(like_movie, as_list=True, code=200, description="OK")
    def delete(self, movie_id):

        return like_movie_service.delete(movie_id)

