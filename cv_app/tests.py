from django.test import TestCase
from django.urls import resolve

from cv_app.views import index


# Create your tests here.

class MainPageTest(TestCase):

    def test_index(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'first_name': 'Adam'})
        self.assertIn('Adam', response.content.decode())