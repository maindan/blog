from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=250, null=False)
    subtitle = models.CharField(max_length=300, null=False)
    content = models.TextField(null=False, max_length=3000)
    tags = models.ManyToManyField('Tag', related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Tag(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=500, null=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
