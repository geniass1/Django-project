from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


def index(request):
    if len(request.GET)==0  or request.GET['a'] == '2':
        tasks = Product.objects.order_by('-id')
    else:
        tasks = Product.objects.order_by('-price')
    return render(request, 'main/index.html', {'title': 'Lol', 'tasks': tasks})


def task_id(request, id):
    task = Product.objects.get(id=id)
    return render(request, 'main/task.html', {'task': task})


def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        form.save()
        return redirect('/')
    form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)


def delete(request, id):
    obj = Product.objects.get(id=id)
    obj.delete()
    return redirect('/')
