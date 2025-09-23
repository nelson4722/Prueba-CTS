from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=30)
    verificado = models.BooleanField(default=False)
    ganador = models.BooleanField(default=False)
    puntos = models.IntegerField(default=0)