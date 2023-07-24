"""Posts models."""

from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from apps.categorias.models import Categoria
from apps.users.models import Profile

class Post(models.Model):
    """Post model."""
    
    user = models.ForeignKey(User, on_delete = models.PROTECT)

    titulo = models.CharField(max_length=255, null=False)
    subtitulo = models.CharField(max_length=255, null=True, blank=True)
    imagen = models.ImageField(null=True, blank=True, upload_to='media', default='static/post-defaul.png')
    texto = RichTextField(null=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    publicado = models.DateTimeField(auto_now=True)
    is_draft = models.BooleanField(default=True)
    url = models.SlugField(max_length=255, unique=True)
    views = models.PositiveIntegerField(default=0)
    categoria = models.ManyToManyField(Categoria, null=True, default='Sin Categoria')

    class Meta:
        ordering = ('publicado',)


    def __str__(self):
        """Return titulo and user."""
        return '{} by @{}'.format(self.titulo, self.user.username)


    def save(self, *args, **kwargs):
        self.url = slugify(self.titulo)
        super(Post, self).save(*args, **kwargs)

