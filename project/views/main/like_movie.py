from flask import request
from flask_restx import Namespace, Resource
from project.container import like_movie_service
from project.models import LikeMovie, User
from project.helpers.decorators import user_required, auth_required


api = Namespace('favorite/movies')

@api.route('/<int:movie_id>')
class LikeMovieView(Resource):

    @auth_required
    def post(self, movie_id) -> LikeMovie:
        """
        Create movie_like
        """
        user = user_required()
        new_data = {
            "user_id": user.id,
            "movie_id": movie_id
        }
        return like_movie_service.create(new_data)



