from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


class Persona(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    text = models.TextField()

    def __str__(self):
        return f"{self.id}: {self.text[:50]}..."


class Simulation(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    policy = models.TextField()

    def __str__(self):
        return f"{self.id}: {self.policy[:50]}..."


class Reaction(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    simulation = models.ForeignKey(Simulation, on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    system_prompt = models.TextField()
    user_prompt = models.TextField()
    text = models.TextField()

    def __str__(self):
        return f"{self.id}: {self.text[:50]}..."
