# Generated by Django 5.1.4 on 2025-01-02 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_remove_agent_first_name_remove_agent_last_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lead',
            old_name='lead',
            new_name='agent',
        ),
    ]