from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task, DoneTask
from django.utils import timezone

# Create your views here.
def index(request):
    return HttpResponse("<h1>This is testing</h1>")

def add_todo(request):
    if request.method == 'POST':
        t = request.POST['content']
        current = timezone.now()
        Task.objects.create(task=t, date_started=current)

    return redirect('homepage')

def delete_todo(request, todo_id):
    if request.method == 'POST':
        tasks = Task.objects.all()
        tasks.get(id=todo_id).delete()

    return redirect('homepage')
