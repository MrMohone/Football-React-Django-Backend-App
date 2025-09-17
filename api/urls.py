from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('country', CountryViewset, basename='country')
router.register('league', LeagueViewset, basename='league')
router.register('characterstic', CharactersticViewset, basename='characterstic')



urlpatterns = router.urls
