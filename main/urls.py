from django.urls import path

from main import views


urlpatterns = [
    path("", views.SimulationCreate.as_view(), name="index"),
]
