from django.contrib import admin
from .models import Post, Tag, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'created_at',)
    search_fields = ('title', 'created_by',)
    list_filter = ('title',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_at', 'updated_at')
    search_fields = ('created_at',)