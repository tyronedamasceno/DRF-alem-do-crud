from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response
from core.filters import DogFilterSet

from core.models import Dog
from core.serializers import DogSerializer, UserSerializer


class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    filterset_class = DogFilterSet

    @action(detail=True)
    def owner(self, request, pk):
        dog = self.get_object()
        serializer = UserSerializer(dog.owner)
        return Response(serializer.data)
