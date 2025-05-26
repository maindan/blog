from rest_framework import serializers
from blog.models import Post, Tag, Comment

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']
class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Tag.objects.all(), write_only=True, source='tags'
    )
    created_by = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'subtitle', 'content',
            'created_at', 'updated_at', 'created_by',
            'tags', 'tag_ids'
        ]

    def get_created_by(self, obj):
        return obj.created_by.username
class CommentSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['id', 'post', 'content', 'created_by', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']