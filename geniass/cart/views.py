from django.shortcuts import render, redirect, get_object_or_404
from main.models import Product
from .models import Order, OrderItem
from django.contrib import messages


def add_to_cart(request, id):
    product = Product.objects.get(id=id)
    order_item, status = OrderItem.objects.get_or_create(product=product)
    user_order, status = Order.objects.get_or_create(owner=request.user, is_ordered=False)
    user_order.items.add(order_item)
    user_order.save()
    messages.info(request, "item added to cart")
    return redirect('main:main')


def check_cart(request):
    order = Order.objects.get(owner=request.user, is_ordered=False)
    return render(request, 'cart/cart.html', {'order': order})


def delete_cart(request, id):
    del_item = OrderItem.objects.filter(id=id)
    del_item.delete()
    return redirect('cart:check_cart')
