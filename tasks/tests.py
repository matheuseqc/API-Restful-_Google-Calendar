from django.test import TestCase
from datetime import date, time
from .models import Task

class TaskAPITestCase(TestCase):
    def test_create_task(self):
        response = self.client.post('/api/tasks/', {'title': 'New Task', 'date': '2024-09-16', 'time': '09:00:00'})
        self.assertEqual(response.status_code, 201)
        
        task = Task.objects.first()
        self.assertIsNotNone(task)
        self.assertEqual(task.title, 'New Task')
        self.assertEqual(task.date, date(2024, 9, 16))  # Comparando com datetime.date
        self.assertEqual(task.time, time(9, 0))  # Comparando com datetime.time
