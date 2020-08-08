from django.db import IntegrityError
from django.test import TestCase
from django.urls import resolve, reverse

from cv_app.views import index
from cv_app.models import CV


# Create your tests here.

class UnitTest(TestCase):

    def test_index(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')
        response = self.client.get('/select/edit/')
        self.assertTemplateUsed(response, 'edit.html')
        response = self.client.get('/select/')
        self.assertTemplateUsed(response, 'select.html')
        response = self.client.get('/new_cv/')
        self.assertTemplateUsed(response, 'new_cv.html')
        response = self.client.get('/view/')
        self.assertTemplateUsed(response, 'view.html')
        response = self.client.get('/blog/')
        self.assertTemplateUsed(response, 'blog.html')

    def test_display_html(self):
        response = self.client.get('/new_cv/display/')
        self.assertTemplateUsed(response, 'display.html')
        response = self.client.get('/view/display/')
        self.assertTemplateUsed(response, 'display.html')

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

    def test_can_use_same_name(self):
        cv1 = CV(username='Adam001', first_name='Adam', last_name='Cart')
        cv2 = CV(username='Adam002', first_name='Adam', last_name='Cart')
        cv1.save()
        cv2.save()
        self.assertEqual('Adam', CV.objects.get(username='Adam001').first_name)
        self.assertEqual('Adam', CV.objects.get(username='Adam002').first_name)
        cv1.delete()
        cv2.delete()

    def test_link_to_create(self):
        select_url = reverse("select")
        response = self.client.get(select_url)
        index_url = reverse("index")
        self.assertContains(
            response, 'href="{0}"'.format(index_url)
        )

    def test_display_to_select(self):
        display_url = reverse("display")
        response = self.client.get(display_url)
        select_url = reverse("select")
        self.assertContains(
            response, 'href="{0}"'.format(select_url)
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

    def test_navigate(self):
        index_url = reverse("index")
        response = self.client.get(index_url)
        select_url = reverse("select")
        self.assertContains(
            response, 'href="{0}"'.format(select_url)
        )
        home_url = reverse("index")
        self.assertContains(
            response, 'href="{0}"'.format(home_url)
        )
        blog_url = reverse("blog")
        self.assertContains(
            response, 'href="{0}"'.format(blog_url)
        )
