from django.shortcuts import render, redirect, get_object_or_404
from main.models import Product
from .models import Order, OrderItem
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


def add_to_cart(request, id):
    product = Product.objects.get(id=id)
    order_item, status = OrderItem.objects.get_or_create(product=product)
    user_order, status = Order.objects.get_or_create(owner=request.user, is_ordered=False)
    user_order.items.add(order_item)
    user_order.save()
    messages.info(request, "item added to cart")
    return redirect('main:main')


def check_cart(request):
    # breakpoint()
    if len(Order.objects.all()) != 0:
        order = Order.objects.get(owner=request.user)
    else:
        order = []
    return render(request, 'cart/cart.html', {'order': order})


def delete_cart(request, id):
    del_item = OrderItem.objects.filter(id=id)
    del_item.delete()
    return redirect('cart:check_cart')


@csrf_exempt
def checkout(request):
    order = Order.objects.get(owner=request.user)
    if request.method == 'POST':
        current_orders = [product.product for product in order.items.all()]
        request.user.catalog.add(*current_orders)
        Order.objects.all().delete()
        return redirect('cart:paid_orders')
    return render(request, 'cart/checkout.html', {'order': order})


def paid_orders(request):
    catalog = request.user.catalog.all()
    return render(request, 'cart/paid_orders.html', {'catalog': catalog})
