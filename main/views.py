from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic.edit import CreateView

from main import models, llm


class SimulationCreate(CreateView):
    model = models.Simulation
    fields = ["policy"]
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["persona_list"] = models.Persona.objects.all()
        context["simulation_list"] = models.Simulation.objects.all().order_by("-id")
        return context

    def get_success_url(self):
        return reverse("simulation_detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        self.object = form.save()
        llm.create_reactions(self.object, self.object.policy)
        return super().form_valid(form)


class SimulationDetail(DetailView):
    model = models.Simulation
