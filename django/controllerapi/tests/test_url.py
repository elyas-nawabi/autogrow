from rest_framework.test import APITestCase,URLPatternsTestCase
from rest_framework import status
from django.urls import include, path, reverse
from ..models import Task

class TaskTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/v1/',include('controllerapi.urls')),
    ]

    def test_create_task(self):
        """
        Ensure we can create a new task object.
        """
        url = reverse('tasklist')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(len(response.data), 1)

class URLTests(APITestCase):

    def test_homepage(self):
        response = self.client.get(reverse("tasklist"))
        self.assertEqual(response.status_code, 200)
    
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/api/v1/tasks/")
        self.assertEqual(response.status_code, 200)