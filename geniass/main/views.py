from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm


def index(request):
    if request.GET.get('search'):
        search = request.GET.get('search')
        index_by_date = f'/?a=2&search={search}'
        index_by_price = f'/?a=1&search={search}'
        tasks = Product.objects.all().filter(title=search)
    else:
        search = ""
        index_by_date = '/?a=2'
        index_by_price = '/?a=1'
        tasks = Product.objects.order_by('-price')
    if 'a' not in request.GET or len(request.GET) == 0 or request.GET['a'] == '2':
        tasks = tasks.order_by('-price')
    elif request.GET['a'] == '1':
        tasks = tasks.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Lol', 'tasks': tasks, 'index_by_date': index_by_date,'index_by_price': index_by_price,'search':search})


def login(request):
    context = {}
    return render(request, 'main/login.html', context)


@csrf_exempt
def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'main/register.html', context)


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
