"""imubaba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from rest_framework import routers,permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from babaapi import views

router = routers.DefaultRouter()
router.register(r'todo', views.TodoViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'group', views.GroupViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="我是你爸爸OpenAPI",
      default_version='v1.0',
      description="我是你爸爸项目的API描述文档",
      terms_of_service="https://mingotech.github.io/",
      contact=openapi.Contact(email="mingo"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),

    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    
    # 请求风格: /work?id=2
    path('work', views.GetWorksByRange),

    # 请求风格: /work/1
    path('work/<int:id>', views.GetWorkById),
    path('work/count/<int:start>', views.CountWork),
    path('work/name/<str:name>', views.QueryWorkByName),
    path('work/key/<str:key>', views.SearchWorkByContent),

    path('work/add', views.AddWork),
    path('work/update', views.UpdateWork),
    path('work/delete', views.DeleteWork),

    # path('docs/', schema_view, name='docs'),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^docs/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
