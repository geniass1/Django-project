from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm, CreateUserForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from hashlib import sha256


@login_required(login_url='login')
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


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.info(request, 'Password or username is incorrect')
    context = {}
    return render(request, 'main/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')


@csrf_exempt
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Accaunt was created')
            return redirect('login')
    context = {'form': form}
    return render(request, 'main/register.html', context)


def change_user_info(request):
    if request.method == 'POST':
        username = request.POST.get('old_username')
        password = request.POST.get('old_password')
        new_username = request.POST.get('new_username')
        new_password = request.POST.get('new_password')
        user = User.objects.get(username=username)
        if user.check_password(password):
            user.username = new_username
            user.set_password(new_password)
            user.save()
            return redirect('login')
        else:
            messages.info(request, 'password is incorrect')
    return render(request, 'main/change_user_info.html')


@login_required(login_url='login')
def task_id(request, id):
    task = Product.objects.get(id=id)
    return render(request, 'main/task.html', {'task': task})


@login_required(login_url='login')
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
