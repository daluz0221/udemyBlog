from django.db import models

from model_utils.models import TimeStampedModel

class Home(TimeStampedModel):
    """Model definition for Home."""

    title = models.CharField('Titulo', max_length=50)
    description = models.TextField('Descripcion')
    about_title = models.CharField('Titulo Nosotros', max_length=50)
    about_text = models.TextField('Texto Nosotros')
    contact_email = models.EmailField('Email de Contacto', max_length=254, blank=True, null=True)
    phone = models.CharField('Telefono Contacto', max_length=20)


    class Meta:
        verbose_name = 'Pagina Principal'
        verbose_name_plural = 'Pagina Principal'

    def __str__(self):
        """Unicode representation of Home."""
        return self.title
    

class Suscribers(TimeStampedModel):
    """Model definition for Suscribers."""

    email = models.EmailField('Email', max_length=254)


    class Meta:
        """Meta definition for Suscribers."""

        verbose_name = 'Suscriptor'
        verbose_name_plural = 'Suscriptores'

    def __str__(self):
        """Unicode representation of Suscribers."""
        return self.email
    


class Contact(TimeStampedModel):
    """Model definition for Contact."""

    full_name = models.CharField('Nombres', max_length=60)
    email = models.EmailField('Email', max_length=254)
    message = models.TextField('Mensaje')


    class Meta:
        """Meta definition for Contact."""

        verbose_name = 'Contacto'
        verbose_name_plural = 'Mensajes de Contacto'

    def __str__(self):
        """Unicode representation of Contact."""
        return self.full_name
