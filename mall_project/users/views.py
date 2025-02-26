# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import User
from django.http import HttpResponse

def register(request):
    """用户注册"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        phone = request.POST['phone']
        user = User.objects.create_user(username=username, password=password, phone=phone)
        user.save()
        login(request, user)
        return redirect('products:product_list')
    return render(request, 'users/register.html')

def login_view(request):
    """用户登录"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('products:product_list')
        return HttpResponse("操，用户名或密码错了！")
    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    """用户登出"""
    logout(request)
    return redirect('products:product_list')

@login_required
def profile(request):
    """个人中心"""
    return render(request, 'users/profile.html', {'user': request.user})