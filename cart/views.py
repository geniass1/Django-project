from django.shortcuts import render, redirect, get_object_or_404
from main.models import Product
from .models import Order, OrderItem, PaidOrder
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
        paid_orders = PaidOrder.objects.create()
        # breakpoint()
        idx = 0
        while idx != len(order.items.all()):
            paid_orders.orders.add(order.items.all()[idx])
            idx += 1
        request.user.catalog.add(paid_orders)
        Order.objects.all().delete()
        return redirect('cart:paid_orders')
    return render(request, 'cart/checkout.html', {'order': order})


def paid_orders(request):
    catalog = request.user.catalog.all()
    catalog = catalog.order_by('-id')
    # idx = 0
    # while idx != len(catalog):
    #     prom = []
    #     for i in catalog[idx].orders.all():
    #         prom.append(i.product.title)
    #     current_products.append(prom)
    #     idx += 1
    return render(request, 'cart/paid_orders.html', {'catalog': list(catalog)})
