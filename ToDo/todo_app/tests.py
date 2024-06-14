from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Task
from .forms import TaskForm

class TaskViewTests(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client = Client()
        self.client.login(username='testuser', password='password')
        
        # Create a test task
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            status='pending',
            user=self.user
        )

    def test_task_list_view(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/tasks-list.html')
        self.assertContains(response, 'Test Task')

    def test_task_create_view_get(self):
        response = self.client.get(reverse('task_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/task-form.html')

    def test_task_create_view_post(self):
        response = self.client.post(reverse('task_create'), {
            'title': 'New Task',
            'description': 'New Description',
            'status': 'pending'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('task_list'))
        self.assertTrue(Task.objects.filter(title='New Task').exists())

    def test_task_edit_view_get(self):
        response = self.client.get(reverse('task_edit', args=[self.task.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/task-form.html')
    
    def test_task_edit_view_post(self):
        response = self.client.post(reverse('task_edit', args=[self.task.pk]), {
            'title': 'Updated Task',
            'description': 'Updated Description',
            'status': 'completed'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('task_list'))
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task')
        self.assertEqual(self.task.status, 'completed')

    def test_task_delete_view_get(self):
        response = self.client.get(reverse('task_delete', args=[self.task.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/task-confirm-delete.html')
    
    def test_task_delete_view_post(self):
        response = self.client.post(reverse('task_delete', args=[self.task.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('task_list'))
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())
