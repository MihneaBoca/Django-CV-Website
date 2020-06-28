from django.test import TestCase
from django.urls import resolve

from cv_app.views import index
from cv_app.models import CV


# Create your tests here.

class MainPageTest(TestCase):

    def test_index(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

    def test_can_save_to_database(self):
        cv1 = CV(first_name='Adam')
        cv2 = CV(first_name='Jessica')
        cv1.save()
        cv2.save()
        self.assertEqual('Adam', CV.objects.get(first_name='Adam').first_name)
        cv1.delete()
        cv2.delete()