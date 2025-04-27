from rest_framework import viewsets
from .serializers import PostSerializer, TagSerializer
from .models import Post, Tag

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class TagView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer