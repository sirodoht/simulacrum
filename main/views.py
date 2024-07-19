from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView

from main import models


class SimulationCreate(SuccessMessageMixin, CreateView):
    model = models.Simulation
    fields = ["policy"]
    template_name = "main/index.html"
    success_message = "simulation complete"
    success_url = "/"
