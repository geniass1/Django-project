from django.shortcuts import render, redirect
from main.models import Product
from .models import Order, OrderItem
from django.contrib import messages


def add_to_cart(request, id):
    product = Product.objects.get(id=id)
    lol = OrderItem.objects.filter(product=product)
    order_item, status = OrderItem.objects.get_or_create(product=product)
    user_order, status = Order.objects.get_or_create(owner=request.user, is_ordered=False)
    user_order.items.add(order_item)
    user_order.save()
    messages.info(request, "item added to cart")
    return redirect('cart:ca')


