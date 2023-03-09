import pytest

from unittest.mock import MagicMock

from project.models import Movie
from project.dao.main import MoviesDAO
from project.services.movies_service import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MoviesDAO(None)

    movie_01 = Movie(id=1, title="first", description="one", trailer="no_one", year=2001, rating=1.0, genre_id=1,
                     director_id=1)

    movie_dao.get_by_id = MagicMock(return_value=movie_01)
    movie_dao.get_all = MagicMock(return_value=[movie_01, "test"])
    movie_dao.create = MagicMock(return_value="Create string")
    movie_dao.update_movie = MagicMock(return_value={
        "id": 12,
        "title": "twelfth",
        "description": "12",
        "trailer": "12",
        "year": 2012,
        "rating": 2012,
        "genre_id": 12,
        "director_id": 12
    })
    movie_dao.delete = MagicMock()

    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_mock(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_item(1)

        assert movie is not None
        assert type(movie) is type(Movie())
        assert movie.title == 'first'
        assert movie.year > 2000
        assert movie.year < 2002

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert movies is not None
        assert type(movies) is list
        assert movies[0].id == 1
        assert movies[1] == 'test'
        assert movies[0].trailer == 'no_one'

    def test_create(self):
        mov_d = {
            "id": 12,
            "name": "twelfth"
        }

        movie = self.movie_service.create(mov_d)

        assert movie is not None
        assert type(movie) is str
        assert movie == "Create string"

    def test_update(self):
        mov_d = {
            "id": 12,
            "title": "twelfth",
            "description": "12",
            "trailer": "12",
            "year": 2012,
            "rating": 2012,
            "genre_id": 12,
            "director_id": 12
        }

        movie = self.movie_service.update(mov_d)

        assert movie is not None
        assert type(movie) is dict
        assert movie.get("title") == "twelfth"
        assert "title" in movie
        assert movie["id"] > 1
        assert movie["id"] == 12
        assert type(movie) is type(mov_d)

    def test_delete(self):
        mov = self.movie_service.delete(1)

        assert mov is None
