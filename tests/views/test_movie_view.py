import pytest

from project.models import Movie


class TestMoviesViews:

    @pytest.fixture
    def movie(self, db):
        obj = Movie(
            title="mov_1",
            description="desc_1",
            trailer="trai_1",
            year=2001,
            rating=1.0
        )
        db.session.add(obj)
        db.session.commit()
        return obj

    def test_many(self, client, movie):
        response = client.get("/movies/")
        assert response.status_code == 200
        assert response.json == [{
            "id": movie.id,
            "title": movie.title,
            "description": movie.description,
            "trailer": movie.trailer,
            "year": movie.year,
            "rating": movie.rating
        }]
