from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Project, Task

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']

class TaskForm(forms.ModelForm):
    # 去掉 widget，直接用 FileField 支持多文件
    files = forms.FileField(required=False, label='上传文件（可多选）')
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'assigned_to', 'due_date']