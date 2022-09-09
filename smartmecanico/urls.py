
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
# Routers provide an easy way of automatically determining the URL conf.


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_auth.urls')),
    path('', include('app_address.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
