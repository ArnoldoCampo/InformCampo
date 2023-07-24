from django.contrib import admin

# Register your models here.
from apps.comentarios.models import Comentario

@admin.register(Comentario)
class CommentAdmin(admin.ModelAdmin):
    """Commentario admin."""

    list_display = ('id', 'user', 'post', 'comentario')
