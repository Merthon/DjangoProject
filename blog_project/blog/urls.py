# blog/urls.py
from django.urls import path
from . import views

app_name = 'blog'  # 设置命名空间，方便模板中反向解析 URL

urlpatterns = [
    path('', views.post_list, name='post_list'),             # 文章列表页，根路径
    path('<slug:slug>/', views.post_detail, name='post_detail'),  # 文章详情页，根据 slug 匹配
]
