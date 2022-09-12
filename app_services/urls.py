from rest_framework import routers
from .views import ServiceModelViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.SimpleRouter()
router.register(r'services', ServiceModelViewSet, basename='services')

urlpatterns = []

urlpatterns += router.urls
