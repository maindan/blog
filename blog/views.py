from rest_framework import viewsets
from .serializers import PostSerializer, TagSerializer
from .models import Post, Tag
from rest_framework.response import Response
from rest_framework.decorators import action

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=False, methods=['get'], url_path='tag/(?P<tag_id>\d+)')
    def filter_by_tag(self, request, tag_id=None):
        posts = Post.objects.filter(tags__id=tag_id)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class TagView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer