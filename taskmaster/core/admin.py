from django.contrib import admin
from .models import Project, Task, TaskFile

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(TaskFile)