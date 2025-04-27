from rest_framework import serializers
from blog.models import Post, Tag, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class CommentSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['id', 'post', 'content', 'created_by', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']