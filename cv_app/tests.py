from django.test import TestCase
from django.urls import resolve

from cv_app.views import index


# Create your tests here.

class MainPageTest(TestCase):

    def test_index(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))