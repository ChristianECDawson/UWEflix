# Generated by Django 3.1.7 on 2023-01-15 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_viewing_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viewing',
            name='duration',
        ),
    ]