from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project, Task, TaskFile
from .forms import UserRegisterForm, ProjectForm, TaskForm

def home(request):
    if request.user.is_authenticated:
        projects = Project.objects.filter(owner=request.user)
        return render(request, 'core/home.html', {'projects': projects})
    return redirect('login')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        messages.error(request, '用户名或密码错误')
    return render(request, 'core/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}，注册成功，快登录！')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'core/register.html', {'form': form})

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    tasks = Task.objects.filter(project=project)
    return render(request, 'core/project_detail.html', {'project': project, 'tasks': tasks})

@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'core/project_form.html', {'form': form})

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, project__owner=request.user)
    files = TaskFile.objects.filter(task=task)
    return render(request, 'core/task_detail.html', {'task': task, 'files': files})

@login_required
def task_create(request, project_id):
    project = get_object_or_404(Project, pk=project_id, owner=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            files = request.FILES.getlist('files')
            for f in files:
                TaskFile.objects.create(task=task, file=f)
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm()
    return render(request, 'core/task_form.html', {'form': form, 'project': project})