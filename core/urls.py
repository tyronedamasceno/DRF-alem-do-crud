from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.viewsets import DogViewSet

router = DefaultRouter()
router.register('dogs', DogViewSet)


urlpatterns = [
    path('api/', include(router.urls))
]