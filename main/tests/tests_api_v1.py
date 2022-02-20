from django.test import TestCase
from django.test import Client
from http import HTTPStatus
from main import factories


class BaseTestCase(TestCase):
    def setUp(self):
        client = Client()
        factories.MyModelFactory(date='2022-01-30', distance=20)
        factories.MyModelFactory(date='2022-02-03', distance=25)
        factories.MyModelFactory(date='2022-02-05', distance=30)
        factories.MyModelFactory(date='2022-02-10', distance=35)
        factories.MyModelFactory(date='2022-02-12', distance=10)

    def auth_headers(self):
        pass


class APITestCase(BaseTestCase):

    def test_routes(self):
        # access routes
        response = self.client.get('/filter-api/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_list_my_model(self):
        # allow objects listing without filter
        response = self.client.get('/filter-api/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(
            len(response.json()['data']), 5
        )

    def test_filter_my_model(self):
        # allow my_model filtering with date, distance

        # test simple single field filter
        response = self.client.get(
            '/filter-api/?search_phrase=distance lt 10'
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(
            len(response.json()['data']), 0
        )

        response = self.client.get(
            '/filter-api/?search_phrase=distance gt 10'
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(
            len(response.json()['data']), 4
        )

        # test against complex phrase
        response = self.client.get(
            '/filter-api/?search_phrase=(date eq 2022-01-30) AND '
            '((distance gt 15) OR (distance lt 10))'
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(
            len(response.json()['data']), 1
        )

    def test_filter_with_non_allowed_fields(self):
        # do not allow my_model filtering with non allowed field id

        response = self.client.get(
            '/filter-api/?search_phrase=id lt 10'
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(
            len(response.json()['data']), 5
        )
