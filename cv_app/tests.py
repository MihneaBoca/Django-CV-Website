from django.db import IntegrityError
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
        response = self.client.get('/bonus/')
        self.assertTemplateUsed(response, 'bonus.html')
        response = self.client.get('/display/')
        self.assertTemplateUsed(response, 'display_list.html')
        response = self.client.get('/edit/')
        self.assertTemplateUsed(response, 'edit.html')

    def test_can_save_to_database(self):
        cv1 = CV(username='Adam001')
        cv2 = CV(username='Jessica001')
        cv1.save()
        cv2.save()
        self.assertEqual('Adam001', CV.objects.get(username='Adam001').username)
        cv1.delete()
        cv2.delete()

    def test_unique_username(self):
        CV(username='Adam2').save()
        with self.assertRaises(Exception) as raised:
            CV(username='Adam2').save()
        self.assertEqual(IntegrityError, type(raised.exception))