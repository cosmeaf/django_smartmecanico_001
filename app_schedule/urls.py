from rest_framework import routers
from .views import ScheduleModelViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.SimpleRouter()
router.register(r'schedule', ScheduleModelViewSet, basename='schedule')


urlpatterns = []

urlpatterns += router.urls
