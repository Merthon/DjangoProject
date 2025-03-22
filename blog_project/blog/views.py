from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Post
import markdown
from .forms import PostForm, CommentForm

def post_list(request):
    posts = Post.objects.all()
    comment_form = CommentForm()  # 给每篇文章加个评论表单
    return render(request, 'blog/post_list.html', {'posts': posts, 'comment_form': comment_form})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    # 转换文章内容为HTML
    post.content_html = markdown.markdown(post.content, extensions=['extra', 'fenced_code'])  # 支持表格和代码块
    comment_form = CommentForm()
    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', post_id=post.id)
    # 转换每条评论为HTML
    for comment in post.comments.all():
        comment.content_html = markdown.markdown(comment.content, extensions=['extra', 'fenced_code'])
    return render(request, 'blog/post_detail.html', {'post': post, 'comment_form': comment_form})

@login_required  # 限制只有登录用户能发帖
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # 先不提交
            post.author = request.user      # 填入当前用户
            post.save()                     # 再保存
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})

@login_required
def comment_new(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_list')
    return redirect('post_list')  # GET请求直接跳回列表

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('post_list')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('post_list')