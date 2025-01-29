# models.py
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Atualize essa linha
    created_at = models.DateTimeField(auto_now_add=True)  # Data de criação do evento

    def __str__(self):
        return self.name
