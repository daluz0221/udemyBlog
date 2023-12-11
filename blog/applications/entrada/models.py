from django.db import models
from django.conf import settings

from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField

class Category(TimeStampedModel):
    """Model definition for Category."""

    short_name = models.CharField('Nombre Corto', max_length=15, unique=True)
    name = models.CharField('Nombre', max_length=50)

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        """Unicode representation of Category."""
        return self.name


class Tag(TimeStampedModel):
    """Model definition for Tag."""

    name = models.CharField('Nombre', max_length=50)

    class Meta:
        """Meta definition for Tag."""

        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'

    def __str__(self):
        """Unicode representation of Tag."""
        return self.name
    
class Entry(TimeStampedModel):
    """Model definition for Entry."""

    user = models.ForeignKey( settings.AUTH_USER_MODEL ,verbose_name='Usuario', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='Categoria', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, verbose_name='Etiquetas')
    title = models.CharField('Titulo', max_length=50)
    photo = models.ImageField('Imagen', upload_to='Entry')
    summary = models.TextField('Resumen')
    body = RichTextUploadingField('Contenido')
    public = models.BooleanField(default=False)
    imagen = models.ImageField('Imagen', upload_to='Entry', blank=True, null=True)
    portada = models.BooleanField(default=False)
    in_home = models.BooleanField(default=False)
    slug = models.SlugField(editable=False, max_length=300)

    class Meta:
        """Meta definition for Entry."""

        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'

    def __str__(self):
        """Unicode representation of Entry."""
        return self.title