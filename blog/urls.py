from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog import views

router = DefaultRouter()
router.register('post', views.PostView, basename='post')
router.register('tag', views.TagView, basename='tag')
router.register('comment', views.CommentView, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('post/<int:post_id>/comments/', views.CommentByPostListView.as_view(), name='post-comments-list'),
]