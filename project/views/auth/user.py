from flask import request
from flask_restx import Resource, Namespace

from project.models import UserSchema

from project.container import user_service


api = Namespace('users')


@api.route('/')
class UsersView(Resource):
    def get(self):
        all_users = user_service.get_all()
        res = UserSchema(many=True).dump(all_users)

        return res, 200


@api.route('/<int:uid>')
class UserView(Resource):
    def get(self, uid):
        b = user_service.get_one(uid)
        sm_d = UserSchema().dump(b)
        return sm_d, 200

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
