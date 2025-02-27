from django.urls import path
from analysis import views

urlpatterns = [
    # 定义 API 接口路由
    path('analyze/', views.analyze_fate, name='analyze_fate'),
]
