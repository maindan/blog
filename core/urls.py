from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from drf_yasg.views import get_schema_view 
from drf_yasg import openapi
from rest_framework import permissions 

schema_view = get_schema_view( 
   openapi.Info( 
      title= "Título da sua API" , 
      default_version= 'v1' , 
      description= "Descrição do teste" , 
      terms_of_service= "https://www.google.com/policies/terms/" , 
      contact=openapi.Contact(email= "contact@yourapi.local" ), 
      license=openapi.License(name= "Licença BSD" ), 
   ), 
   public= True , 
   permission_classes=(permissions.AllowAny,), 
) 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('', include('blog.urls')),
    path('', include('account.urls')),
    path( 'swagger/' , schema_view.with_ui( 'swagger' , cache_timeout= 0 ), name= 'schema-swagger-ui' ), 
    path( 'redoc/' , schema_view.with_ui( 'redoc' , cache_timeout= 0 ), name= 'schema-redoc' ), 
    path( 'swagger.json' , schema_view.without_ui(cache_timeout= 0 ), name= 'schema-json' ), 
    
]
