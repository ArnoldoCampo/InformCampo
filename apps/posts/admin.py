from django.contrib import admin

# Register your models here.
from apps.posts.models import Post

@admin.register (Post)

class PostAdmin(admin.ModelAdmin):
    """Post admin."""

    list_display = ('id', 'user', 'titulo', 'subtitulo','imagen')
    search_fields = ('titulo', 'user__username', 'user__email')
    list_filter = ('fecha_creacion','publicado')
        
        
    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ('url', )
        form = super(PostAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['user'].initial = request.user
        #form.base_fields['profile'].initial = request.user.profile
        return form



