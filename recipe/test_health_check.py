from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class HealthCheckTests(APITestCase):
    """Test the health check API."""

    def test_health_check(self):
        url = reverse('health-check')
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)