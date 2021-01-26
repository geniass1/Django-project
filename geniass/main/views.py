from django.shortcuts import render, redirect
from .models import Product
from cart.models import Order
from .forms import ProductForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='user:login')
def index(request):
    if request.GET.get('search'):
        search = request.GET.get('search')
        index_by_date = f'/?a=1&search={search}'
        index_by_price = f'/?a=2&search={search}'
        tasks = Product.objects.all().filter(title=search)
    else:
        search = ""
        index_by_date = '/?a=1'
        index_by_price = '/?a=2'
        tasks = Product.objects.order_by('-price')
    if 'a' not in request.GET or len(request.GET) == 0 or request.GET['a'] == '2':
        tasks = tasks.order_by('-price')
    elif request.GET['a'] == '1':
        tasks = tasks.order_by('-id')
    order = Order.objects.filter(owner=request.user, is_ordered=False)
    try:
        current_orders = [product.product for product in order[0].items.all()]
    except:
        current_orders = []
    paid_orders = request.user.catalog.all()
    return render(request, 'main/index.html', {'tasks': tasks, 'index_by_date': index_by_date,
                                               'index_by_price': index_by_price,
                                               'search':search,'current_orders':current_orders,
                                               'paid_orders':paid_orders})


@login_required(login_url='user.views.login')
def task_id(request, id):
    task = Product.objects.get(id=id)
    return render(request, 'main/task.html', {'task': task})


@login_required(login_url='user.views.login')
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
