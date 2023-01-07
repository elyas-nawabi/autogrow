# import json
# from rest_framework import status
# from django.test import TestCase, Client
# from rest_framework.test import APITestCase, APIClient
# from django.urls import reverse
# from ..views import TaskList
# from unittest import TestCase
# from unittest.mock import patch

# client = APIClient()

# class TestApi(TestCase):
#     @patch('views.TaskList.get')
#     def test_task_set(self, mock_list_tasks):
#         mock_list_tasks.return_value.status_code = 200
#         mock_list_tasks.return_value.json.return_value = {
#             [{
#                 "id": 2,
#                 "task_id": 2,
#                 "task_name": "task number tow",
#                 "task_type": "simple",
#                 "active": True,
#                 "frequency": "weekly"
#             }]
#         }
#         tasks = TaskList()
#         response = client.get(reverse('tasklist'))
#         assert response.status_code == 200
#         self.assertEquals(response.json()[0]['task_name', 'taskone'])