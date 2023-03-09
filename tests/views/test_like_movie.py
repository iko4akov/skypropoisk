import pytest

from project.models import LikeMovie

class TestLikeMovieView:

    @pytest.fixture
    def like_movie(self, db):
        obj = LikeMovie(user_id=1, movie_id=2)
        db.session.add(obj)
        db.session.commit()
        return obj

    def test_get_all(self, like_movie, client):

        response = client.get('/favorite/movies/')

        assert response.status_code == 200
        assert response.json == [{
            "id": like_movie.id,
            "user_id": like_movie.user_id,
            "movie_id": like_movie.movie_id
                                  }]
