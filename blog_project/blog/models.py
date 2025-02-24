from django.db import models
from django.contrib.auth.models import User

# 分类模型，用于对文章进行分类管理
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="分类名称，必须唯一")
    description = models.TextField(blank=True, null=True, help_text="分类描述，可选")

    def __str__(self):
        return self.name

# 文章模型，包含文章标题、作者、内容、分类、发布时间等字段
class Post(models.Model):
    title = models.CharField(max_length=200, help_text="文章标题")
    slug = models.SlugField(max_length=200, unique=True, help_text="文章唯一标识（用于 URL 中）")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_posts',
        help_text="文章作者，关联 Django 内置用户模型"
    )
    content = models.TextField(help_text="文章正文内容")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="文章所属分类，可为空"
    )
    created = models.DateTimeField(auto_now_add=True, help_text="文章创建时间，自动记录")
    updated = models.DateTimeField(auto_now=True, help_text="文章更新时间，自动更新")

    class Meta:
        ordering = ('-created',)  # 默认按创建时间倒序排列
        verbose_name = '文章'
        verbose_name_plural = '文章列表'

    def __str__(self):
        return self.title

# 评论模型，用于对文章进行评论管理
class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        help_text="关联的文章"
    )
    author = models.CharField(max_length=80, help_text="评论作者名称")
    email = models.EmailField(help_text="评论作者邮箱")
    body = models.TextField(help_text="评论内容")
    created = models.DateTimeField(auto_now_add=True, help_text="评论创建时间")
    active = models.BooleanField(default=True, help_text="评论是否激活（过滤垃圾评论）")

    class Meta:
        ordering = ('created',)
        verbose_name = '评论'
        verbose_name_plural = '评论列表'

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
