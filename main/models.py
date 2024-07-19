from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


class Persona(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    prompt = models.TextField()


class Policy(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    text = models.TextField()

    class Meta:
        verbose_name_plural = "Policies"


class Reaction(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    prompt = models.TextField()
    text = models.TextField()
