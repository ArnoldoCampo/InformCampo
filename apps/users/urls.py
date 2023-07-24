# """Users URLs."""

# # Django
# from django.urls import path
# from django.views.generic import TemplateView
# # View
# from apps.users import views

# urlpatterns = [
#     path(
#         route='login',
#         view = views.LoginView.as_view(),
#         name='login'
#     ),
#     path(
#         route='registro',
#         view = views.SignupView.as_view(),
#         name='registro'
#     ),
#     path(
#         route='logout/',
#         view=views.LogoutView.as_view(),
#         name='logout'
#     ),
#     path(
#         route='registro_completado/',
#         view=TemplateView.as_view(template_name='users/registrok.html'),
#         name='registrok'
#     ),
# ]

from django.urls import path
from django.views.generic import TemplateView
from apps.users.views import SignupView, LoginView, LogoutView
from apps.users import views

urlpatterns = [
    path(
        route='login/',
        view=LoginView.as_view(),
        name='login'
    ),
    path(
        route='registro/',
        view=SignupView.as_view(),
        name='registro'
    ),
    path(
        route='logout/',
        view=LogoutView.as_view(),
        name='logout'
    ),
    path(
        route='registro_completado/',
        view=TemplateView.as_view(template_name='users/registrok.html'),
        name='registrok'
    ),
]




