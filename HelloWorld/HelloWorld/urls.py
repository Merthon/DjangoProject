# 该 Django 项目的 URL 声明; 一份由 Django 驱动的网站"目录"。
from django.urls import path
 
from . import views
 
urlpatterns = [
    path("", views.hello, name="hello"),
]
