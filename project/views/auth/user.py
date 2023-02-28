from flask import request
from flask_restx import Resource, Namespace

from project.container import user_service
from project.setup.api.models import user

api = Namespace('user')


@api.route('/')

class UsersView(Resource):

    @api.marshal_with(user, code=200, as_list=True, description='OK')
    def get(self):
        return user_service.get_all(), 200


@api.route('/<int:uid>')
class UserView(Resource):
    @api.response(404, 'Not Found')
    @api.marshal_with(user, code=200, description='OK')
    def get(self, uid):
        return user_service.get_item(uid), 200


    def put(self, uid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = uid
        user_service.update(req_json)
        return "", 204

    def patch(self, uid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = uid
        user_service.update(req_json)

    # @admin_required
    def delete(self, uid):
        user_service.delete(uid)
        return "", 204
