from rest_framework.routers import SimpleRouter
from api.views import VehicleViewSet, IncidentViewSet, UserViewSet


router = SimpleRouter()
router.register('vehicles', VehicleViewSet, basename='vehicles')
router.register('incidents', IncidentViewSet, basename='incidents')
router.register('users', UserViewSet, basename='users')



urlpatterns = router.urls
