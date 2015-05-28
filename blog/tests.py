from django import http
from django.test import TestCase
from django.test.client import RequestFactory
from blog import views


class HomeViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_home(self):
        request = self.factory.get('/blog/')
        home_view = views.HomeView.as_view()
        response = home_view(request)
        self.assertEqual(200, response.status_code)
