from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog import views

router = DefaultRouter()
router.register('post', views.PostView, basename='post')

urlpatterns = [
    path('', include(router.urls))
]