from django.db import models

class Category(models.Model):
    """商品分类"""
    name = models.CharField(max_length=50, verbose_name="分类名称")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name="父分类")

    class Meta:
        verbose_name = "商品分类"
        verbose_name_plural = "商品分类"

    def __str__(self):
        return self.name

class Product(models.Model):
    """商品"""
    name = models.CharField(max_length=100, verbose_name="商品名称")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="分类")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="价格")
    stock = models.PositiveIntegerField(verbose_name="库存")
    description = models.TextField(verbose_name="商品描述")
    image = models.ImageField(upload_to='products/', verbose_name="商品图片")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="上架时间")

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = "商品"

    def __str__(self):
        return self.name