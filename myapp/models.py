from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Agrega tus campos personalizados aquí
    age = models.PositiveIntegerField(blank=True, null=True)
    bio = models.TextField(blank=True)
