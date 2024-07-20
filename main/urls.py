from django.urls import path

from main import views


urlpatterns = [
    path("", views.SimulationCreate.as_view(), name="simulation_create"),
    path(
        "simulations/<int:pk>/",
        views.SimulationDetail.as_view(),
        name="simulation_detail",
    ),
    path(
        "sentiments/<int:simulation_id>/create/",
        views.sentiment_create,
        name="sentiment_create",
    ),
]
