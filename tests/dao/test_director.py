import  pytest

from project.dao import DirectorsDAO

from project.models import Director

class TestDirectorsDAO:

    @pytest.fixture
    def director_dao(self, db):
        return DirectorsDAO(db.session)

    @pytest.fixture
    def dir_1(self, db):
        dir = Director(name="test")
        db.session.add(dir)
        db.session.commit()
        return dir

    @pytest.fixture
    def dir_2(self, db):
        dir = Director(name="test2")
        db.session.add(dir)
        db.session.commit()
        return dir

    def test_get_director_by_id(self, dir_1, director_dao):
        assert director_dao.get_by_id(dir_1.id) == dir_1

    def test_get_genre_by_id_not_found(self, director_dao):
        assert not director_dao.get_by_id(1)

    def test_get_all_genres(self, director_dao, dir_1, dir_2):
        assert director_dao.get_all() == [dir_1, dir_2]

    def test_get_genres_by_page(self, app, director_dao, dir_1, dir_2):
        app.config['ITEMS_PER_PAGE'] = 1
        assert director_dao.get_all(page=1) == [dir_1, dir_2]
        assert director_dao.get_all(page=2) == [dir_2]
        assert director_dao.get_all(page=3) == []
