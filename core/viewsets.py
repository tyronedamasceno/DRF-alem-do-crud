from rest_framework import viewsets

from core.models import Dog
from core.serializers import DogSerializer


class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

