from rest_framework import viewsets
from rest_framework import generics
from .serializers import PostSerializer, TagSerializer, CommentSerializer
from .models import Post, Tag, Comment
from rest_framework.response import Response
from rest_framework.decorators import action

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class TagView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user) 

    def get_queryset(self):
        return Comment.objects.all()   

    @action(detail=True, methods=['get'], url_path='comments')
    def filter_by_post(self, request, pk=None):
        comments = Comment.objects.filter(post_id=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
class CommentByPostListView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post=post_id)