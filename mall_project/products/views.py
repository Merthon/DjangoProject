# products/views.py
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product, Category

def product_list(request):
    """商品列表（首页）"""
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'products/product_list.html', {'products': products, 'categories': categories})

def product_detail(request, product_id):
    """商品详情"""
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})

def search_products(request):
    """商品搜索"""
    query = request.GET.get('q', '')
    products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'products/product_list.html', {'products': products, 'query': query})

def recommend_products(request):
    """商品推荐"""
    products = Product.objects.order_by('-stock')[:10]
    return render(request, 'products/product_list.html', {'products': products, 'recommend': True})