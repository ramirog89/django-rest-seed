# from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import (
  APIRequestFactory,
  APITestCase,
  URLPatternsTestCase,
  force_authenticate
)

from src.app.models import AccountManager
from src.app.controllers import AccountController

class AccountControllerTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        # self.dummy = User.objects.create_user('dummy', 'dummy@test.com', 'dummy')

    def tearDown(self):
        pass
        # self.dummy.delete()

    def test_account_list(self):
        # user = User.objects.get(username='dummy')
        view = AccountController.as_view({ 'get':'list' })
        request = self.factory.get('/api/account/')
        # force_authenticate(request, user=user)
        response = view(request)

        self.assertEqual(response.status_code, 200)
