# Generated by Django 5.0.7 on 2024-07-19 18:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0005_rename_policy_policy_text"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Simulation",
            new_name="Reaction",
        ),
    ]
