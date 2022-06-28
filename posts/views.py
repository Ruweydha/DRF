from django.shortcuts import render
from .serializers import PostSerializer
from rest_framework import generics
from .models import Post

# Create your views here.
class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
