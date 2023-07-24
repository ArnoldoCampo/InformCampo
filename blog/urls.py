"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
from django.contrib import admin
from django.urls import path
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
]"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include(('apps.posts.urls', 'posts'), namespace='posts')),
    
    path(
        route='about',
        view=TemplateView.as_view(template_name='about-us.html'),
        name='about'
    ),

    path('', include(('apps.users.urls', 'users'), namespace='users')),
    path(
    route='registro_completado/',
    view=TemplateView.as_view(template_name='users/registrok.html'),
    name='registrok'
),
]
