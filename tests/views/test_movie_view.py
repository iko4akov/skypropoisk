import json
from unittest import TestCase, mock
from project.container import movie_service
from project.views.main.movies import MoviesView, MovieView
from project.server import create_app
from tests.test_config import TestingConfig

app = create_app(TestingConfig)

class MoviesViewTestCase(TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.movies_url = '/movies'

    @mock.patch.object(movie_service, 'get_all')
    def test_get_movies_all_success(self, mock_get_all):
        mock_get_all.return_value = [{'id': 1, 'title': 'Movie 1'}, {'id': 2, 'title': 'Movie 2'}]
        response = self.client.get(self.movies_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), [{'id': 1, 'title': 'Movie 1'}, {'id': 2, 'title': 'Movie 2'}])

    @mock.patch.object(movie_service, 'create')
    def test_post_movie_success(self, mock_create):
        mock_create.return_value = {'id': 1, 'title': 'New Movie'}
        data = {'title': 'New Movie'}
        response = self.client.post(self.movies_url, json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers['location'], '/movies/1')
        self.assertEqual(json.loads(response.data), None)

class MovieViewTestCase(TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.movie_url = '/movies/1'

    @mock.patch.object(movie_service, 'get_item')
    def test_get_movie_success(self, mock_get_item):
        mock_get_item.return_value = {'id': 1, 'title': 'Movie 1'}
        response = self.client.get(self.movie_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {'id': 1, 'title': 'Movie 1'})

    @mock.patch.object(movie_service, 'update')
    def test_put_movie_success(self, mock_update):
        data = {'id': 1, 'title': 'Updated Movie'}
        response = self.client.put(self.movie_url, json=data)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(json.loads(response.data), None)
        mock_update.assert_called_once_with(data)

    @mock.patch.object(movie_service, 'delete')
    def test_delete_movie_success(self, mock_delete):
        response = self.client.delete(self.movie_url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(json.loads(response.data), None)
        mock_delete.assert_called_once_with(1)
