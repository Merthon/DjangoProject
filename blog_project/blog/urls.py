from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # 访问/blog/时显示文章列表
    path('new/', views.post_new, name='post_new'), # 发布路径
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
]