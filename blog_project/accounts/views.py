# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm

def register_view(request):
    """
    用户注册视图：
    - GET 请求：展示注册表单
    - POST 请求：验证表单并创建用户，成功后自动登录并重定向
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # 创建用户
            login(request, user)  # 自动登录新用户
            return redirect('/')  # 跳转到首页或其它页面
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})
