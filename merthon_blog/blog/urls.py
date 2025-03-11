from django.urls import path
from .views import PostList, ProjectList, TagList

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('projects/', ProjectList.as_view(), name='project-list'),
    path('tags/', TagList.as_view(), name='tag-list'),
]
