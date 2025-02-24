# blog_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),           # 后台管理路径
    path('', include('blog.urls', namespace='blog')),  # 包含博客应用的 URL 路由
    # 包含 accounts 应用的 URL，访问前缀为 accounts/
    path('accounts/', include('accounts.urls', namespace='accounts')),
]
