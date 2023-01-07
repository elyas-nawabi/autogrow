from asyncio import tasks
import datetime
import email
import json
from rest_framework import status

# from django.test import TestCase, Client
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from ..models import Task, Device, Data

# from ..views import TaskList
from ..serializers import TaskSerializer

# importing unittest.mock
from unittest import TestCase
from unittest.mock import patch, MagicMock
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission, User

User = get_user_model()
# initializing the APIClient app
client = APIClient()


class GetAllTasksTest(APITestCase):
    """Test module for GET all tasks API"""

    def setUp(self):
        test_user1 = User.objects.create(
            username="testuser1", email="testemail@gmail.com", password="123"
        )
        # test_user1 = User.objects.all()
        test_user1.save()
        devices = Device.objects.create(serial=1, name="dd2", user=test_user1)
        devices.save()
        # devices.user.set(test_user1)
        test_task = Task.objects.create(
            id=1,
            name="tsk1",
            _type="onetime",
            active=False,
            frequency="weekly",
            executed=True,
            recurrence_id=1,
            recurrence_rule="hourly",
            recurrence_exceptions="no exception",
            device=devices
        )
        # test_task.device.set(devices)
        # print(test_user1)
        # print(devices)
        # print(test_task)

    def test_get_all_tasks(self):
        # get API response
        response = client.get(reverse("tasklist"))
        # get data from db
        tasks = Task.objects.all()
        # OR:
        # tasks = Task.objects.get(id=1)

        serializer = TaskSerializer(tasks, many=True)
        self.assertEqual(response.data, serializer.data)
        # print(tasks[0].name)
        # self.assertIn(tasks._meta.get_field('name').verbose_name, response.content)
        # self.assertIn(tasks[0].name, response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleTaskTest(APITestCase):
    """Test module for GET single task API"""

    def setUp(self):
        self.single_task = Task.objects.create(
            id=1, name="task19", _type="onetime", active=True, frequency="monthly"
        )   
        self.single_task.save()
    def test_get_valid_single_task(self):
        response = client.get(reverse("taskdetail", kwargs={"pk": self.single_task.id}))
        tasks = Task.objects.get(id=1)
        serializer = TaskSerializer(tasks)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # print(response.data)

    def test_get_invalid_single_task(self):
        response = client.get(reverse("taskdetail", kwargs={"pk": 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        # print(response.data)


class CreateNewTaskTest(APITestCase):
    """Test module for inserting a new task"""

    def setUp(self):
        test_user1 = User.objects.create_user(
            username="testuser1", password="123", email="testemail@gmail.com"
        )
        test_user1.save()
        devices = Device.objects.create(serial=1, name="dd2", user=test_user1)
        self.valid_data = {
            "id": 4,
            "name": "newTask",
            "_type": "onetime",
            "active": False,
            "frequency": "hourly",
            "executed": True,
            "recurrence_id": 10,
            "recurrence_rule": "weekly",
            "recurrence_exceptions": "noexception",
            "device": 1
        }
        self.invalid_data = {
            "id": "not_an_id",
            "name": "",
            "_type": "",
            "active": False,
            "frequency": "minute",
            "executed": True,
            "recurrence_id": 10,
            "recurrence_rule": "weekly",
            "recurrence_exceptions": "noexception",
            "device": 1
        }

    def test_create_valid_task(self):
        response = client.post(
            reverse("tasklist"),
            data=json.dumps(self.valid_data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_task(self):
        response = client.post(
            reverse("tasklist"),
            data=json.dumps(self.invalid_data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleTaskTest(APITestCase):
    """Test module for updating an existing task record"""

    def setUp(self):
        self.single_task = Task.objects.create(
            id=10,
            name="tsk10",
            _type="onetime",
            active=True,
            frequency="monthly"
        )
        self.single_task.save()
        self.valid_data = {
            "id": 10,
            "name": "newUpdatedTask",
            "_type": "onetime",
            "active": False,
            "frequency": "hourly"
        }
        self.invalid_data = {
            "id":1,
            "name": "",
            "_type": "invalid",
            "active": "",
            "frequency": ""
        }

    def test_valid_update_task(self):
        response = client.put(
            reverse("taskdetail", kwargs={"pk": self.single_task.id}),
            data=json.dumps(self.valid_data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_task(self):
        response = client.put(
            reverse("taskdetail", kwargs={"pk": self.single_task.id}),
            data=json.dumps(self.invalid_data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleTaskTest(APITestCase):
    """Test module for deleting an existing task record"""

    def setUp(self):
        self.task99 = Task.objects.create(
            id=99,
            name="tsk99",
            _type="tsktyp99",
            active=True,
            frequency="monthly",
        )

    def test_valid_delete_task(self):
        response = client.delete(
            reverse("taskdetail", kwargs={"pk": self.task99.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_task(self):
        response = client.delete(reverse("taskdetail", kwargs={"pk": 100000}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
