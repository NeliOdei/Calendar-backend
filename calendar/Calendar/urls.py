"""Calendar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib import admin
from rest_framework import routers, authtoken
from django.urls import include, path, re_path

from Calendar.views import Ok

from CalendarApp import views as CalendarApp_views
from rest_framework import permissions
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from CalendarApp.handlers import grpc_handlers as error_grpc_handlers



schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



router = routers.DefaultRouter()
router.register(r'user', CalendarApp_views.UserViewSet)
router.register(r'types', CalendarApp_views.TypesViewSet)
router.register(r'color', CalendarApp_views.ColorsViewSet)
router.register(r'tasks', CalendarApp_views.TasksViewSet)
router.register(r'filter', CalendarApp_views.TaskFilterViewSet, basename='models-of-type')


urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('ok/', Ok.as_view()),
    path('api/user', CalendarApp_views.user, name ='user'),
    path('grpc/', CalendarApp_views.test, name ='test'),
]


def grpc_handlers(server):
    error_grpc_handlers(server)