from flask import request
from flask_restx import Resource, Namespace

from project.container import user_service
from project.setup.api.models import user
from project.helpers.decorators import auth_required
from project.utils import email_required

api = Namespace('user')

@api.route('/')
class UserView(Resource):

    @auth_required
    @api.response(404, 'Not Found')
    @api.marshal_with(user, code=200, description='OK')
    def get(self):
        """
        Get data user
        """
        email = email_required()
        return user_service.get_by_email(email), 200


    @auth_required
    def patch(self):
        """
        Edited only name, surname, favorite_genre, need enter:
        name: ...
        surname: ...
        favourite_genre: ...
        """
        req_json = request.json
        print(req_json)
        email = email_required()
        req_json["email"] = email
        user_service.patch_user(req_json)
        return "", 201


@api.route('/password/')
class User_pas_View(Resource):
    @auth_required
    def put(self):
        """
        Edite only password need enter:
        password_old: ...
        password_new: ...
        """
        req_json = request.json
        print(req_json)
        email = email_required()
        req_json["email"] = email
        user_service.update(req_json)
        return "", 201
