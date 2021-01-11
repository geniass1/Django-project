from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Lol', 'tasks': tasks})


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

