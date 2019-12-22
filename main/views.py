from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task, DoneTask
from django.utils import timezone
from django.contrib import messages

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
        messages.success(request, 'Sucessfully added todo')

    return redirect('homepage')

def delete_todo(request, todo_id):
    if request.method == 'POST':
        tasks = Task.objects.all()
        tasks.get(id=todo_id).delete()
        messages.success(request, 'Sucessfully deleted todo')

    return redirect('homepage')

def completed_todo(request, todo_id):
    if request.method == 'POST':
        tasks = Task.objects.all()
        current = timezone.now()
        t = tasks.get(id=todo_id)
        DoneTask.objects.create(task=t.task, date_started=t.date_started, date_done=current)
        t.delete()
        messages.success(request, 'Congratulations on completing your to do')

    return redirect('homepage')

def undo_todo(request, todo_id):
    if request.method == 'POST':
        done_tasks = DoneTask.objects.all()
        done_task = done_tasks.get(id=todo_id)
        Task.objects.create(task=done_task.task, date_started=done_task.date_started)
        done_task.delete()
        messages.success(request, 'Sucessfully undid todo')

    return redirect('homepage')