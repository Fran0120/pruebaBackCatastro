from rest_framework import routers
from movies_information.api import moviesInformationViewSet

router = routers.DefaultRouter()
router.register('api/movies', moviesInformationViewSet, 'movies')

urlpatterns = router.urls