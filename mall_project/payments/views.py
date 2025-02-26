# payments/views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from orders.models import Order

@login_required
def process_payment(request, order_id):
    """处理支付"""
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        order.status = 'paid'
        order.save()
        return redirect('orders:order_detail', order_id=order.id)
    return render(request, 'payments/pay.html', {'order': order})

def payment_callback(request):
    """支付回调"""
    order_id = request.GET.get('order_id')
    order = Order.objects.get(id=order_id)
    order.status = 'paid'
    order.save()
    return HttpResponse("支付成功，回调已处理！")