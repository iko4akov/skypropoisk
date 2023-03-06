from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example=''),
})


director: Model = api.model('Режиссер', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=255, example=''),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(max_length=255, example=''),
    'description': fields.String(max_length=255, example=''),
    'trailer': fields.String(max_length=255, example=''),
    'year': fields.Integer(),
    'rating': fields.Float(),
})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, max_length=255, example=''),
    # 'password': fields.String(required=True, max_length=255, example=''),
    'name': fields.String(max_length=255, example=''),
    'surname': fields.String(max_length=255, example=''),
    'favorite_genre_id': fields.Integer(example=15),
})

like_movie: Model = api.model("Фильм в избранном", {
    "id": fields.Integer(required=True, example=2),
    "user_id": fields.Integer(required=True, example=1),
    "movie_id": fields.Integer(required=True, example=1),
})
