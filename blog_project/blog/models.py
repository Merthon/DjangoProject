from django.db import models

# 定义文章模型
class Post(models.Model):
    title = models.CharField(max_length=200)  # 文章标题，最长200字符
    content = models.TextField # 文章内容，markdown格式
    created_at = models.DateTimeField(auto_now_add=True) # 自动记录创建时间
    updated_at = models.DateTimeField(auto_now=True)  # 自动更新修改时间

    def __str__(self):
        return self.title   # 后台显示时用标题表示对象