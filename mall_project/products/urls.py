from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.product_list, name='product_list'),          # 商品列表（首页）
    path('<int:product_id>/', views.product_detail, name='product_detail'),  # 商品详情
    path('search/', views.search_products, name='search'),      # 搜索
    path('recommend/', views.recommend_products, name='recommend'),  # 推荐
]