from rest_framework import routers
from .views import AddressModelViewSet, AddressGenericViewSet
# Routers provide an easy way of automatically determining the URL conf.
router = routers.SimpleRouter()
router.register(r'address', AddressModelViewSet, basename='address')
router.register(r'list_address', AddressGenericViewSet,
                basename='list_address')

urlpatterns = []

urlpatterns += router.urls
