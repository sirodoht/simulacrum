# Generated by Django 5.0.7 on 2024-07-19 19:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0009_simulation_reaction_simulation"),
    ]

    operations = [
        migrations.AddField(
            model_name="reaction",
            name="completed_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
