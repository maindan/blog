from django.contrib import admin
from .models import Post, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'created_at',)
    search_fields = ('title', 'created_by',)
    list_filter = ('title',)
@admin.register(Tag)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)