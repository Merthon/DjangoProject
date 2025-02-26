from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """自定义用户模型，替换默认auth.User"""
    phone = models.CharField(max_length=11, unique=True, verbose_name="手机号")
    address = models.TextField(blank=True, null=True, verbose_name="收货地址")
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name="头像")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="注册时间")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户"

    def __str__(self):
        return self.username