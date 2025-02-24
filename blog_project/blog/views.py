from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import CommentForm

def post_list(request):
    """
    文章列表视图：
    - 获取所有文章（企业项目中可考虑只显示已发布文章）
    - 渲染模板，并传递文章列表数据
    """
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, slug):
    """
    文章详情视图：
    - 根据 slug 获取对应文章
    - 处理评论表单提交（POST 请求）
    - 获取文章所有激活状态的评论
    - 渲染详情模板并传递文章、评论、以及评论表单数据
    """
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        # 如果是提交评论的表单
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # 生成 Comment 对象但暂不提交数据库
            new_comment = comment_form.save(commit=False)
            new_comment.post = post  # 将评论与当前文章关联
            new_comment.save()       # 保存评论到数据库
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    }
    return render(request, 'blog/post_detail.html', context)
