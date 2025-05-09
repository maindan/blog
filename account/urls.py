from django.urls import path, include
from rest_framework.routers import DefaultRouter
from account import views

router = DefaultRouter()
router.register('user', views.UserViewSet, basename='User')

urlpatterns = [
    path('', include(router.urls)),
    # path('register/', UserCreateAPIView.as_view(), name='user-register'),
]