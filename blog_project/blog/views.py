from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()  # 查出所有文章
    return render(request, 'blog/post_list.html', {'posts': posts})  # 传到模板渲染