from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('register/', views.register, name='register'),  # 注册
    path('login/', views.login_view, name='login'),      # 登录
    path('logout/', views.logout_view, name='logout'),   # 登出
    path('profile/', views.profile, name='profile'),     # 个人中心
]