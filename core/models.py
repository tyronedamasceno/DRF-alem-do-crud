from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE


class Person(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)


class Dog(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)    
