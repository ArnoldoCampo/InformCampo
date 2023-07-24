from django.contrib import admin

# Register your models here.
from apps.categorias.models import Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    """Categoria admin."""

    list_display = ('id', 'nombre')