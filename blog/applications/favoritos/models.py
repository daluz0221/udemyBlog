from django.db import models
from django.conf import settings

from model_utils.models import TimeStampedModel

from applications.entrada.models import Entry



class Favoritos(TimeStampedModel):
    """Model definition for Favoritos."""

    user = models.ForeignKey( settings.AUTH_USER_MODEL ,verbose_name='Usuario', on_delete=models.CASCADE)
    entry = models.ForeignKey(Entry, verbose_name='Entrada', on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Favoritos."""
        unique_together = ('user', 'entry')

        verbose_name = 'Favorito'
        verbose_name_plural = 'Favoritos'

    def __str__(self):
        """Unicode representation of Favoritos."""
        return self.title