from django.db import IntegrityError
from django.test import TestCase
from django.urls import resolve, reverse

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

    def test_link_to_create(self):
        select_url = reverse("select")
        response = self.client.get(select_url)
        index_url = reverse("index")
        self.assertContains(
            response, 'href="{0}"'.format(index_url)
        )

    def test_link_to_edit(self):
        select_url = reverse("select")
        response = self.client.get(select_url)
        edit_url = reverse("edit")
        self.assertContains(
            response, 'href="{0}"'.format(edit_url)
        )

    def test_back_from_create(self):
        index_url = reverse("index")
        response = self.client.get(index_url)
        select_url = reverse("select")
        self.assertContains(
            response, 'href="{0}"'.format(select_url)
        )

    def test_back_from_edit(self):
        edit_url = reverse("edit")
        response = self.client.get(edit_url)
        select_url = reverse("select")
        self.assertContains(
            response, 'href="{0}"'.format(select_url)
        )