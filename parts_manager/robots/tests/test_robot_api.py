from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from parts_manager.robots.factories import RobotFactory


class RobotApiTests(APITestCase):

    def setUp(self):
        super(RobotApiTests, self).setUp()

        self.user = User.objects.create_superuser(
            'testuser',
            'test@example.com',
            'test'
        )

    def test_get_robot_list(self):
        self.client.login(username=self.user.username, password='test')

        url = reverse('api:robot-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.content)

    def test_get_robot_detail(self):
        self.client.login(username=self.user.username, password='test')

        robot = RobotFactory()

        url = reverse('api:robot-detail', args=[robot.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
