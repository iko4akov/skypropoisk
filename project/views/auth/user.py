from flask import request
from flask_restx import Resource, Namespace

from project.container import user_service
from project.setup.api.models import user
from project.helpers.decorators import auth_required, user_required

api = Namespace('user')

@api.route('/')
class UserView(Resource):

    @auth_required
    @user_required
    @api.response(404, 'Not Found')
    @api.marshal_with(user, code=200, description='OK')
    def get(self, email):
        """
        Get data user
        """
        print(email)
        return user_service.get_by_email(email), 200


    @auth_required
    def patch(self):
        """
        Edited only name, surname, favorite_genre, need enter:
        email: ...
        name: ...
        surname: ...
        favorite_genre: ...
        """
        req_json = request.json
        user_service.patch_user(req_json)
        return "Данные изменены или добавлены", 201


@api.route('/password')
class User_pas_View(Resource):
    @auth_required
    def put(self):
        """
        Edite only password need enter:
        email: ...
        password_old: ...
        password_new: ...
        password_new_retry: ...
        """
        req_json = request.json

        return user_service.update(req_json), 201
