from flask import request
from flask_restx import Resource, Namespace

from project.container import user_service
from project.setup.api.models import user
from project.helpers.decorators import auth_required

api = Namespace('user/product')


@api.route('/')

class ProductUserstView(Resource):

    @api.marshal_with(user, code=200, as_list=True, description='OK')
    def get(self):
        return user_service.get_all(), 200


@api.route('/<int:uid>')
class ProductUserView(Resource):
    @api.response(404, 'Not Found')
    @api.marshal_with(user, code=200, description='OK')
    def get(self, uid):
        return user_service.get_item(uid), 200


    # @admin_required
    def delete(self, uid):
        user_service.delete(uid)
        return "", 204
