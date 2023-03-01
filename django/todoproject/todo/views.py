from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import TodoModel
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class TodoList(LoginRequiredMixin, ListView):
    template_name = 'list.html'
    model = TodoModel
    login_url = reverse_lazy('login')
    
class TodoDetails(LoginRequiredMixin ,DetailView):
    template_name = 'detail.html'
    model = TodoModel

class TodoCreate(LoginRequiredMixin, CreateView):
    template_name = 'create.html'
    model = TodoModel #データの格納先
    fields = ('category','title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')
    
class TodoDelete(LoginRequiredMixin, DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')
    
class TodoUpdate(LoginRequiredMixin, UpdateView):
    template_name = "update.html"
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')
    
# Create your views here.
