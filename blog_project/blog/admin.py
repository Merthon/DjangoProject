from django.contrib import admin
from .models import Post, Category, Comment

# 定义文章后台管理显示配置
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'updated')  # 后台列表页显示的字段
    prepopulated_fields = {'slug': ('title',)}  # 自动根据标题生成 slug

# 定义分类后台管理显示配置
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

# 定义评论后台管理显示配置
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created', 'active')
    list_filter = ('active', 'created')
    search_fields = ('author', 'email', 'body')

# 注册模型到后台管理系统
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
