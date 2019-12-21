from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task, DoneTask
from django.utils import timezone

# Create your views here.
def index(request):
    tasks = Task.objects.all().order_by("-date_started")
    done_tasks = DoneTask.objects.all().order_by("-date_done")
    return render(request, 'main/index.html', {'tasks': tasks, 'done_tasks': done_tasks})

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
