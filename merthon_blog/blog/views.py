from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Project, Tag
from .serializers import PostSerializer, ProjectSerializer, TagSerializer

# 文章列表 API
class PostList(APIView):
    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

# 项目列表 API
class ProjectList(APIView):
    def get(self, request, format=None):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

# 标签列表 API
class TagList(APIView):
    def get(self, request, format=None):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
