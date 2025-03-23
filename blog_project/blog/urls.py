from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # 访问/blog/时显示文章列表
    path('<int:post_id>/', views.post_detail, name='post_detail'),  # 详情页路径
    path('new/', views.post_new, name='post_new'), # 发布路径
    path('edit/<int:post_id>/', views.post_edit, name='post_edit'),    # 编辑路径
    path('delete/<int:post_id>/', views.post_delete, name='post_delete'),  # 删除路径
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
]