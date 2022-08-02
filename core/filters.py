from django_filters import rest_framework as filters

from core.models import Dog


class DogFilterSet(filters.FilterSet):
    class Meta:
        model = Dog
        fields = {
            "id": ["exact"],
            "name": ["icontains"]
        }
