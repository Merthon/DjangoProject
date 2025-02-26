# orders/views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from products.models import Product

@login_required
def cart_view(request):
    """购物车"""
    cart = request.session.get('cart', {})
    items = []
    total = 0
    for product_id, qty in cart.items():
        product = Product.objects.get(id=product_id)
        subtotal = product.price * qty
        total += subtotal
        items.append({'product': product, 'quantity': qty, 'subtotal': subtotal})
    return render(request, 'orders/cart.html', {'items': items, 'total': total})

@login_required
def add_to_cart(request, product_id):
    """添加到购物车"""
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    cart[product_id] = cart.get(product_id, 0) + 1
    request.session['cart'] = cart
    return redirect('orders:cart')

@login_required
def remove_from_cart(request, item_id):
    """从购物车移除"""
    cart = request.session.get('cart', {})
    if str(item_id) in cart:
        del cart[str(item_id)]
    request.session['cart'] = cart
    return redirect('orders:cart')

@login_required
def checkout(request):
    """结算"""
    cart = request.session.get('cart', {})
    if not cart:
        return HttpResponse("操，购物车是空的！")
    total = 0
    order = Order.objects.create(user=request.user, total_amount=0)
    for product_id, qty in cart.items():
        product = Product.objects.get(id=product_id)
        subtotal = product.price * qty
        total += subtotal
        OrderItem.objects.create(order=order, product=product, quantity=qty, price=product.price)
    order.total_amount = total
    order.save()
    request.session['cart'] = {}
    return redirect('payments:process_payment', order_id=order.id)

@login_required
def order_detail(request, order_id):
    """订单详情"""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    items = OrderItem.objects.filter(order=order)
    return render(request, 'orders/order_detail.html', {'order': order, 'items': items})