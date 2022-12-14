
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
#
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Smart-Mecânico API",
        default_version='v1',
        description="Smart Mecânico é uma plataforma online que conecta de maneira rápida, simples e objetiva o consumidor a prestação de serviços",
        terms_of_service="https://smartmecanico.com.br/politica-de-privacidade/",
        contact=openapi.Contact(email="contato@smartmecanico.com.br"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',
                                         cache_timeout=0), name='schema-swagger-ui'),
    path('', schema_view.with_ui('redoc',
                                 cache_timeout=0), name='schema-redoc'),
    path('api/v1/', include('app_auth.urls')),
    path('api/v1/', include('app_address.urls')),
    path('api/v1/', include('app_vehicles.urls')),
    path('api/v1/', include('app_services.urls')),
    path('api/v1/', include('app_schedule.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
