# from django.shortcuts import render
# from django.views.generic import FormView
# from django.urls import reverse, reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth import views as auth_views

# # Forms
# from apps.users.forms import SignupForm


# class SignupView(FormView):
#     """Users sign up view."""

#     template_name = 'users/registro.html'
#     form_class = SignupForm
#     success_url = reverse_lazy('users:registrok')

#     def form_valid(self, form):
#         """Save form data."""
#         form.save()
#         return super().form_valid(form)


# class LoginView(auth_views.LoginView):
#     """Login view."""
#     template_name = 'users/login.html'


# class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
#     """Logout view."""
#     template_name = 'users/logout.html'



# from django.shortcuts import render, redirect

# from django.views.generic import FormView
# from django.urls import reverse, reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth import views as auth_views
# from django.contrib import messages
# from django.contrib.auth.models import User
# from apps.users.models import Profile

# # Forms
# from apps.users.forms import SignupForm


# class SignupView(FormView):
#     template_name = 'users/registro.html'
#     form_class = SignupForm
#     success_url = reverse_lazy('users:registrok')

#     def form_valid(self, form):
#         username = form.cleaned_data['username']
#         if User.objects.filter(username=username).exists():
#             messages.error(self.request, "This username is already taken")
#             return redirect('registrok')
#         user = form.save()
#         profile = Profile.objects.create(user=user)
#         # Aquí puedes realizar cualquier otra lógica de procesamiento del formulario, si es necesario
#         return super().form_valid(form)

# class LoginView(auth_views.LoginView):
#     """Login view."""
#     template_name = 'users/login.html'


# class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
#     """Logout view."""
#     template_name = 'users/logout.html'


from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.contrib.auth.models import User
from apps.users.forms import SignupForm
from apps.users.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin


from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.contrib.auth.models import User
from apps.users.models import Profile

# Forms
from apps.users.forms import SignupForm

class SignupView(FormView):
    template_name = 'users/registro.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:registrok')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            messages.error(self.request, "This username is already taken")
            return redirect('users:registro')
        
        # Creamos el usuario
        user = form.save()
        
        # Creamos el perfil solo si no existe
        if not hasattr(user, 'profile'):
            profile = Profile.objects.create(user=user)
            
        # Aquí puedes realizar cualquier otra lógica de procesamiento del formulario, si es necesario
        return super().form_valid(form)

class LoginView(auth_views.LoginView):
    template_name = 'users/login.html'

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    template_name = 'users/logout.html'


