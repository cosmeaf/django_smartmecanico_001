from rest_framework import routers
from .views import AddressModelViewSet
# Routers provide an easy way of automatically determining the URL conf.
router = routers.SimpleRouter()
router.register(r'address', AddressModelViewSet, basename='address')
# router.register(r'address', AddressGenericViewSet, basename='address')

urlpatterns = []

urlpatterns += router.urls
