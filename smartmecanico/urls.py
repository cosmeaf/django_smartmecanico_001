"""smartmecanico URL Configuration

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
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
# Routers provide an easy way of automatically determining the URL conf.

from .views import UserViewSet
from app_address.views import AddressViewSet
from app_vehicle.views import VehicleViewSet
from app_service.views import ServiceViewSet
from app_schedule.views import ScheduleViewSet
from app_hour.views import hourAvailableViewSet
from rest_framework import routers
from .views import UserViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'address', AddressViewSet, basename='address')
router.register(r'service', ServiceViewSet, basename='service')
router.register(r'vehicle', VehicleViewSet, basename='vehicle')
router.register(r'hour', hourAvailableViewSet, basename='hour')
router.register(r'schedule', ScheduleViewSet, basename='schedule')

schema_view = get_schema_view(
    openapi.Info(
        title="Smart Mecânico API",
        default_version='v1',
        description="Service Appointment for Mechanic in Home",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="connta"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^api/v1/swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/v1/swagger/', schema_view.with_ui('swagger',
                                                cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/redoc/', schema_view.with_ui('redoc',
                                              cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    # path('api/v1/', include('address.urls'), name='address'),
    # path('api/v1/', include('vehicle.urls'), name='vehicle'),
    # path('api/v1/', include('app_service.urls'), name='service'),
    # path('api/v2/', user_api_view, name='users'),
    # path('api/v2/<int:pk>/', user_api_view_detail, name='users_details'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
