import unittest
import json
from app import app
from database import init_db, get_db_connection

class TestTaskAPI(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Запускаем сервер Flask перед тестами."""
        init_db()
    
    def setUp(self):
        """Создаем клиент для тестирования."""
        self.client = app.test_client()
        self.client.testing = True

    def test_create_task(self):
        """Тестируем создание задачи."""
        response = self.client.post('/task', data=json.dumps({
            'title': 'Test Task',
            'description': 'This is a test task.'
        }), content_type='application/json')
        
        self.assertEqual(response.status_code, 201)
        self.assertIn('Task created successfully!', response.get_data(as_text=True))

    def test_get_tasks(self):
        """Тестируем получение всех задач."""
        response = self.client.get('/tasks')
        self.assertEqual(response.status_code, 200)
        tasks = json.loads(response.get_data(as_text=True))
        self.assertIsInstance(tasks, list)

    def test_update_task(self):
        """Тестируем обновление задачи."""
        response = self.client.post('/task', data=json.dumps({
            'title': 'New Task',
            'description': 'Description of the task.'
        }), content_type='application/json')
        
        task_id = 1  # Используем id первой задачи, если она была создана
        response = self.client.put(f'/task/{task_id}', data=json.dumps({
            'title': 'Updated Task',
            'description': 'Updated description.',
            'completed': 1
        }), content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('Task updated successfully!', response.get_data(as_text=True))

    def test_delete_task(self):
        """Тестируем удаление задачи."""
        response = self.client.post('/task', data=json.dumps({
            'title': 'Delete Task',
            'description': 'Task to be deleted.'
        }), content_type='application/json')
        
        task_id = 1  # Предположим, что id задачи == 1
        response = self.client.delete(f'/task/{task_id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Task deleted successfully!', response.get_data(as_text=True))

    def test_mark_task_as_completed(self):
        """Тестируем пометку задачи как выполненной."""
        response = self.client.post('/task', data=json.dumps({
            'title': 'Complete Task',
            'description': 'Task to be completed.'
        }), content_type='application/json')
        
        task_id = 1  # Предположим, что id задачи == 1
        response = self.client.put(f'/task/{task_id}/complete')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Task marked as completed!', response.get_data(as_text=True))

