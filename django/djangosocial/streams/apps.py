"""Streams app config."""

from django.apps import AppConfig


class StreamsConfig(AppConfig):
    """Defaault streams app config."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "djangosocial.streams"
