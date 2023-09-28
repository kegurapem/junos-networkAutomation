from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')


class UsuarioNornir(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # password = models.CharField(max_length=50)
    administrador = models.BooleanField(default=False)

    class Meta:
        db_table = 'usuario_nornir'
