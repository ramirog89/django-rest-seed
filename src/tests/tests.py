from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import (
  APIRequestFactory,
  APITestCase,
  URLPatternsTestCase,
  force_authenticate
)

from ..app.controllers import PostList

class PostListTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.dummy = User.objects.create_user('dummy', 'dummy@test.com', 'dummy')

    def tearDown(self):
        self.dummy.delete()

    def test_authorized_get(self):
        user = User.objects.get(username='dummy')
        view = PostList.as_view()
        request = self.factory.get('/api/posts/')
        force_authenticate(request, user=user)
        response = view(request)

        self.assertEqual(response.status_code, 200)
