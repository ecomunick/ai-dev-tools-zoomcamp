from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import TODO

# Create your views here.
class TodoListView(ListView):
    model = TODO
    template_name = 'todos/home.html'
    context_object_name = 'todos'

class TodoCreateView(CreateView):
    model = TODO
    template_name = 'todos/todo_form.html'
    fields = ['title', 'description', 'due_date']
    success_url = reverse_lazy('todo_list')

class TodoUpdateView(UpdateView):
    model = TODO
    template_name = 'todos/todo_form.html'
    fields = ['title', 'description', 'due_date', 'resolved']
    success_url = reverse_lazy('todo_list')

class TodoDeleteView(DeleteView):
    model = TODO
    template_name = 'todos/todo_confirm_delete.html'
    success_url = reverse_lazy('todo_list')

def toggle_resolved(request, pk):
    todo = get_object_or_404(TODO, pk=pk)
    todo.resolved = not todo.resolved
    todo.save()
    return redirect('todo_list')
