import jwt
from flask import request, abort

from instance.config import BaseConfig
from project.container import user_service


def auth_required(func):
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)

        data = request.headers["Authorization"]
        token = data.split("Bearer ")[-1]

        try:
            jwt.decode(token, BaseConfig.PWD_HASH_SALT, algorithms=[BaseConfig.JWT_ALGO])

        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)

        return func(*args, **kwargs)

    return wrapper

def user_required(func):
    def wrapper(*args, **kwargs):

        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]

        user = jwt.decode(token, BaseConfig.PWD_HASH_SALT, algorithms=[BaseConfig.JWT_ALGO])

        email = user['email']
        user_id = user_service.get_by_email(email).id

        user["id"] = user_id

        return func(user=user, *args, **kwargs)

    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)

        data = request.headers["Authorization"]
        token = data.split("Bearer ")[-1]
        role = None

        try:
            user = jwt.decode(token, BaseConfig.PWD_HASH_SALT, algorithms=[BaseConfig.JWT_ALGO])
            role = user.get("role", "user")

        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)

        if role != "admin":
            abort(403)

        return func(*args, **kwargs)

    return wrapper
