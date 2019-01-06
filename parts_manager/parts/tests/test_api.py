from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from parts_manager.website.factories import UserFactory
from parts_manager.parts.factories import PartFactory


class PartsApiTests(APITestCase):

    def setUp(self):
        super(PartsApiTests, self).setUp()

        self.user = UserFactory()

    def test_get_parts_list(self):
        self.client.login(username=self.user.username, password='test')

        url = reverse('api:part-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_parts_detail(self):
        self.client.login(username=self.user.username, password='test')

        part = PartFactory()

        url = reverse('api:part-detail', args=[part.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
