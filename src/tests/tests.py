from django.contrib.auth.models import User
from rest_framework.test import (
  APIRequestFactory,
  APITestCase,
  URLPatternsTestCase,
  force_authenticate
)

from ..app.views import HelloView

class HelloWorldTest(APITestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = APIRequestFactory()
        self.dummy = User.objects.create_user('dummy', 'dummy@test.com', 'dummy')

    def tearDown(self):
        self.dummy.delete()

    def test_unauthorized_get(self):
        # Create an instance of a GET request.
        request = self.factory.get('/hello_world/')
        # Simulate anonymous user
        # Use this syntax for class-based views.
        response = HelloView.as_view()(request)
        # Assertion
        self.assertEqual(response.status_code, 401)

    def test_authorized_get(self):
        user = User.objects.get(username='dummy')
        view = HelloView.as_view()
        request = self.factory.get('/hello_world/')
        force_authenticate(request, user=user)
        response = view(request)

        self.assertEqual(response.status_code, 200)
