from rest_framework.routers import SimpleRouter
from api.views import VehicleViewSet, IncidentViewSet


router = SimpleRouter()
router.register('vehicles', VehicleViewSet, basename='vehicles')
router.register('incidents', IncidentViewSet, basename='incidents')


urlpatterns = router.urls
