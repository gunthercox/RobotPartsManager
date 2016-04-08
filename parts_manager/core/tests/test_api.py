from rest_framework.test import APITestCase
from rest_framework import status
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class ApiTests(APITestCase):

    def setUp(self):
        super(ApiTests, self).setUp()

        self.user = User.objects.create_superuser(
            'testuser',
            'test@example.com',
            'test'
        )

    def test_get_api_root(self):
        self.client.login(username=self.user.username, password='test')

        url = reverse('api:api-root')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
