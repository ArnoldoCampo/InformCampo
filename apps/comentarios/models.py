from django.db import models
from django.contrib.auth.models import User
from apps.posts.models import Post

# Model

# Create your models here.
class Comentario(models.Model):
    """Comentario model."""
    
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    profile = models.ForeignKey('users.Profile', on_delete=models.PROTECT)
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    comentario = models.CharField(max_length=5000)

    def __str__(self):
        return self.comentario
