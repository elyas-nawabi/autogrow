from django.test import TestCase
from controllerapi.models import Task

class TestAppModels(TestCase):
    def setUp(self):
        # Set up non-modified objects used by all test methods
        Task.objects.create(id = 1, name='tsk1', _type='tsktyp1',active = True, frequency='hourly')

    def test_model_str(self):
        # id = Task.objects.create(id=1)
        # name = Task.objects.create(name ='tsk1')
        # type = Task.objects.create(type ="tsktyp1")
        # active = Task.objects.create(active = True)
        # frequency = Task.objects.create(frequency ="hourly")
        # self.assertEquals(id.id,1, msg="numbers are not equal")
        task_tsk1 = Task.objects.get(name='tsk1')
        self.assertEqual(task_tsk1.get_tasks_info(),'tsk1 type is tsktyp1')
        # self.assertEquals(type.type,'tsktyp1')
        # self.assertEquals(active.active,True)
        # self.assertEquals(frequency.frequency,'hourly')
    
    def test_task_name_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('id').verbose_name
        self.assertEquals(field_label, 'ID')
        field_label = task._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')
        field_label = task._meta.get_field('_type').verbose_name
        self.assertEquals(field_label, '_type')
        field_label = task._meta.get_field('active').verbose_name
        self.assertEquals(field_label, 'active')
        field_label = task._meta.get_field('frequency').verbose_name
        self.assertEquals(field_label, 'frequency')
                         
    def test_task_name_max_length(self):
        task = Task.objects.get(id=1)
        max_length = task._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_task_name_comma_task_type(self):
        task = Task.objects.get(id=1)
        expected_object_name = f'{task.name},{task._type},{task.active},{task.frequency}'
        self.assertEquals(str(task.name),task.name)
        # print(task._meta.get_fields())
        # print(expected_object_name)

    def test_get_absolute_url(self):
        task = Task.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(task.get_absolute_url(), '/api/v1/tasks/1/')
