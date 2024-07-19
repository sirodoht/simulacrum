from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjUserAdmin

from main import models


@admin.register(models.User)
class UserAdmin(DjUserAdmin):
    list_display = (
        "id",
        "username",
        "email",
    )
    search_fields = ("username", "email")
    ordering = ["-id"]


@admin.register(models.Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "prompt",
    )
    search_fields = (
        "id",
        "prompt",
    )
    ordering = ["-id"]


@admin.register(models.Simulation)
class SimulationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "policy",
    )
    search_fields = (
        "id",
        "policy",
    )
    ordering = ["-id"]


@admin.register(models.Reaction)
class ReactionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "simulation",
        "persona",
        "prompt",
    )
    search_fields = (
        "id",
        "prompt",
        "text",
    )
    ordering = ["-id"]
