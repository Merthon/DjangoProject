from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 加作者字段

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    '''
    增加评论功能
    '''
     # 关联到文章
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments') 
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 评论者
    content = models.TextField()  # 评论内容
    created_at = models.DateTimeField(auto_now_add=True)  # 评论时间

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"