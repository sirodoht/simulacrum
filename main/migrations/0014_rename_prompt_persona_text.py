# Generated by Django 5.0.7 on 2024-07-19 20:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0013_remove_reaction_prompt_reaction_system_prompt_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="persona",
            old_name="prompt",
            new_name="text",
        ),
    ]
