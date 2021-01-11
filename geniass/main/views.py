from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Lol', 'tasks': tasks})


def task_id(request, id):
    task = Task.objects.get(id=id)
    return render(request, 'main/task.html', {'task': task})


def create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        form.save()
        return redirect('/')
    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)


def delete(request, id):
    obj = Task.objects.get(id=id)
    obj.delete()
    return redirect('/')
