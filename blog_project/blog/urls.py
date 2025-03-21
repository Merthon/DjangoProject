from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # 访问/blog/时显示文章列表
]