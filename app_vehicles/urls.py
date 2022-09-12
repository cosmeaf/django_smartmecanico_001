from rest_framework import routers
from .views import VehicleModelViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.SimpleRouter()
router.register(r'vehicle', VehicleModelViewSet, basename='vehicle')


urlpatterns = []

urlpatterns += router.urls
