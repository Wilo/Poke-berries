from django.conf import settings

from rest_framework.routers import DefaultRouter, SimpleRouter
from app.api.views import BerryViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register(r"allBerryStats", BerryViewSet, "Get All Berries")

app_name = "api"
urlpatterns = router.urls
