from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from lab6.views import AuthorViewSet, PublisherViewSet, BookViewSet  # Замените bookstore на фактическое имя вашего приложения
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny



router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'publishers', PublisherViewSet)
router.register(r'books', BookViewSet)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Your API Title",
        default_version='v1',
        description="API for your application",
    ),
    public=True,
    permission_classes=[permissions.IsAuthenticated],  # Доступ к Swagger только для авторизованных
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
]
