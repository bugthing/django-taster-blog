import sys
from django.test import Client
from django.contrib.auth.models import User
from django.test import TestCase

from blog.models import Posting

class BaseTestCase(TestCase):
    def login_test_user(self):
        self.client = Client()
        self.username = 'test'
        self.email='test@test.com'
        self.password = 'test'        
        self.test_user = User.objects.create_user(self.username, self.email, self.password)
        self.client.login(username=self.username, password=self.password)

    def create_posting(self):
        self.test_posting = Posting(content='test post one')
        self.test_posting.save()
        return self.test_posting

class PostingModelTest(TestCase):
    def test_create(self):
        Posting(content='Test').save()
        self.assertEqual(1, len(Posting.objects.all()))
        self.assertEqual('Test', Posting.objects.all()[0].content)

class BlogViewTest(BaseTestCase):
    def setUp(self):
        self.create_posting()

    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('test post one' in resp.content)

    def test_new_form(self):
        self.login_test_user()
        resp = self.client.get('/form/new')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('<form' in resp.content)

    def test_edit_form(self):
        self.login_test_user()
        resp = self.client.get('/form/' + str(self.test_posting.id))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(self.test_posting.content in resp.content)

    def test_new(self):
        self.login_test_user()
        resp = self.client.post('/update/new',  {'content': 'test post two'})
        self.assertEqual(302, resp.status_code)
        self.assertEqual(2, Posting.objects.count())

    def test_update(self):
        self.login_test_user()
        resp = self.client.post('/update/' + str(self.test_posting.id),  {'content': 'test post two - again'})
        self.assertEqual(resp.status_code, 302)
        reloaded_post = Posting.objects.get(id=self.test_posting.id)
        self.assertEqual(reloaded_post.content, 'test post two - again')

    def test_del(self):
        self.login_test_user()
        resp = self.client.post('/delete/' + str(self.test_posting.id),  {'content': 'test post two - again'})
        self.assertEqual(resp.status_code, 302)
        self.assertRaises(Posting.DoesNotExist, Posting.objects.get, id=self.test_posting.id)

    def test_login(self):
        resp = self.client.post('/login', {'username': 'benjamin', 'password': 'p4ssw0rd'})
        self.assertEqual(resp.status_code, 302)
