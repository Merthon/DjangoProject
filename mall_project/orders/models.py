from django.db import models
from users.models import User
from products.models import Product

class Order(models.Model):
    """订单"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="下单用户")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="总金额")
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', '待支付'),
            ('paid', '已支付'),
            ('shipped', '已发货'),
            ('completed', '已完成'),
            ('cancelled', '已取消'),
        ],
        default='pending',
        verbose_name="订单状态"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = "订单"

    def __str__(self):
        return f"订单 {self.id} - {self.user.username}"

class OrderItem(models.Model):
    """订单详情"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="所属订单")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="商品")
    quantity = models.PositiveIntegerField(verbose_name="数量")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="单价")

    class Meta:
        verbose_name = "订单项"
        verbose_name_plural = "订单项"

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
