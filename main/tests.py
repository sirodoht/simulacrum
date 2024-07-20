from unittest.mock import patch
from django.test import TestCase
from django.urls import reverse


from main import models


class SimulationCreateTest(TestCase):
    def setUp(self):
        self.policy = "Example policy"

    @patch("main.llm.create_reactions")
    def test_simulation_create_view_post(self, mock_create_reactions):
        response = self.client.post(
            reverse("simulation_create"), {"policy": self.policy}
        )
        simulation = models.Simulation.objects.get(policy=self.policy)

        mock_create_reactions.assert_called_once_with(simulation, self.policy)
        self.assertRedirects(
            response, reverse("simulation_detail", kwargs={"pk": simulation.pk})
        )
        self.assertEqual(models.Simulation.objects.count(), 1)
        self.assertEqual(models.Simulation.objects.first().policy, self.policy)
