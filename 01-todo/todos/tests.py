from django.test import TestCase
from django.urls import reverse
from datetime import date, timedelta
from .models import TODO

# Create your tests here.
class TODOModelTest(TestCase):
    def test_create_todo(self):
        """Test creating a TODO item"""
        todo = TODO.objects.create(
            title="Test TODO",
            description="Test description",
            due_date=date.today() + timedelta(days=7)
        )
        self.assertEqual(todo.title, "Test TODO")
        self.assertEqual(todo.description, "Test description")
        self.assertFalse(todo.resolved)
        
    def test_todo_str_method(self):
        """Test the string representation of TODO"""
        todo = TODO.objects.create(title="Test TODO")
        self.assertEqual(str(todo), "Test TODO")
        
    def test_todo_default_resolved_false(self):
        """Test that resolved defaults to False"""
        todo = TODO.objects.create(title="Test TODO")
        self.assertFalse(todo.resolved)

class TODOViewsTest(TestCase):
    def setUp(self):
        """Create test data"""
        self.todo1 = TODO.objects.create(
            title="Test TODO 1",
            description="Description 1",
            due_date=date.today() + timedelta(days=7)
        )
        self.todo2 = TODO.objects.create(
            title="Test TODO 2",
            resolved=True
        )
        
    def test_todo_list_view(self):
        """Test the TODO list view"""
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test TODO 1")
        self.assertContains(response, "Test TODO 2")
        
    def test_todo_create_view_get(self):
        """Test GET request to create view"""
        response = self.client.get(reverse('todo_create'))
        self.assertEqual(response.status_code, 200)
        
    def test_todo_create_view_post(self):
        """Test POST request to create a new TODO"""
        response = self.client.post(reverse('todo_create'), {
            'title': 'New TODO',
            'description': 'New description',
            'due_date': date.today() + timedelta(days=3)
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertTrue(TODO.objects.filter(title='New TODO').exists())
        
    def test_todo_update_view(self):
        """Test updating a TODO"""
        response = self.client.post(
            reverse('todo_edit', args=[self.todo1.pk]),
            {
                'title': 'Updated TODO',
                'description': 'Updated description',
                'due_date': date.today() + timedelta(days=10),
                'resolved': True
            }
        )
        self.assertEqual(response.status_code, 302)
        self.todo1.refresh_from_db()
        self.assertEqual(self.todo1.title, 'Updated TODO')
        self.assertTrue(self.todo1.resolved)
        
    def test_todo_delete_view(self):
        """Test deleting a TODO"""
        todo_id = self.todo1.pk
        response = self.client.post(reverse('todo_delete', args=[todo_id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(TODO.objects.filter(pk=todo_id).exists())
        
    def test_toggle_resolved(self):
        """Test toggling the resolved status"""
        # Initially False
        self.assertFalse(self.todo1.resolved)
        
        # Toggle to True
        response = self.client.get(reverse('todo_toggle', args=[self.todo1.pk]))
        self.assertEqual(response.status_code, 302)
        self.todo1.refresh_from_db()
        self.assertTrue(self.todo1.resolved)
        
        # Toggle back to False
        response = self.client.get(reverse('todo_toggle', args=[self.todo1.pk]))
        self.todo1.refresh_from_db()
        self.assertFalse(self.todo1.resolved)
        
    def test_todo_ordering(self):
        """Test that TODOs are ordered by created_at descending"""
        response = self.client.get(reverse('todo_list'))
        todos = response.context['todos']
        # Most recent should be first
        self.assertEqual(todos[0].pk, self.todo2.pk)
        self.assertEqual(todos[1].pk, self.todo1.pk)
