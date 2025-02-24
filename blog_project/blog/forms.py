# blog/forms.py
from django import forms
from .models import Comment

# 定义评论表单，基于 Comment 模型创建
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # 指定表单包含的字段
        fields = ('author', 'email', 'body')
        # 可添加字段的 widgets 或验证规则
        widgets = {
            'body': forms.Textarea(attrs={'rows': 4, 'placeholder': '请输入评论内容'}),
        }
