from django.urls import path
from . import views

app_name = 'payments'
urlpatterns = [
    path('pay/<int:order_id>/', views.process_payment, name='process_payment'),  # 处理支付
    path('callback/', views.payment_callback, name='payment_callback'),          # 支付回调
]