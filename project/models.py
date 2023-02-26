from sqlalchemy import Column, String, Integer, Float, ForeignKey
from marshmallow import Schema, fields
from sqlalchemy.orm import relationship

from project.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)


class Director(models.Base):
    __tablename__ = 'director'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)


class Movie(models.Base):
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(String(255))
    trailer = Column(String(255))
    year = Column(Integer)
    rating = Column(Float)
    genre_id = Column(Integer, ForeignKey("genres.id"))
    genre = relationship("Genre")
    director_id = Column(Integer, ForeignKey("director.id"))
    director = relationship("Director")


class User(models.Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    name = Column(String(255))
    surname = Column(String(255))
    favorite_genre = Column(String(255))


class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    password = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    favorite_genre = fields.Str()
