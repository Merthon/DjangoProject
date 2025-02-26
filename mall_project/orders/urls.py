from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    path('cart/', views.cart_view, name='cart'),            # 购物车
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  # 添加到购物车
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),  # 从购物车移除
    path('checkout/', views.checkout, name='checkout'),     # 结算
    path('<int:order_id>/', views.order_detail, name='order_detail'),  # 订单详情
]