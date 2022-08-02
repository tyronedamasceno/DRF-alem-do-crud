from django.contrib.auth import get_user_model
from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE


class Dog(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
