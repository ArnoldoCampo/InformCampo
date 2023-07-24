"""User forms."""

# Django
from django import forms

# Models
from apps.comentarios.models import Comentario
from django.contrib.auth.models import User

class CreateCommentForm(forms.ModelForm):
    """Post model form."""

    coment = forms.CharField(widget=forms.Textarea)


    class Meta:
        """Form settings."""

        model = Comentario
        fields = ('user', 'profile', 'post', 'comentario')
