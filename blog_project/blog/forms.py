from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # 标题和内容

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # 只让用户填内容