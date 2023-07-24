# from django.contrib.auth.models import Group
# from .models import Profile
# from django.dispatch import receiver
# from django.db.models.signals import post_save


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=Profile)
# def add_user_to_registrado_group(sender, instance, created, **kwargs):
#     if created:
#         try:
#             registrado = Group.objects.get(name='registrado')
#         except Group.DoesNotExist:
#             registrado = Group.objects.create(name='registrado')
#         instance.user.groups.add(registrado)

# from django.contrib.auth.models import Group
# from .models import Profile
# from django.dispatch import receiver
# from django.db.models.signals import post_save

# @receiver(post_save, sender=Profile)
# def add_user_to_registrado_group(sender, instance, created, **kwargs):
#     if created:
#         try:
#             registrado = Group.objects.get(name='registrado')
#         except Group.DoesNotExist:
#             registrado = Group.objects.create(name='registrado')
#         instance.user.groups.add(registrado)


# from django.contrib.auth.models import Group
# from .models import Profile
# from django.dispatch import receiver
# from django.db.models.signals import post_save
# from django.contrib.auth.models import User

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.get_or_create(user=instance)

# @receiver(post_save, sender=Profile)
# def add_user_to_registrado_group(sender, instance, created, **kwargs):
#     if created:
#         try:
#             registrado = Group.objects.get(name='registrado')
#         except Group.DoesNotExist:
#             registrado = Group.objects.create(name='registrado')
#         instance.user.groups.add(registrado)

from django.contrib.auth.models import Group
from .models import Profile
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User



@receiver(post_save, sender=Profile)
def add_user_to_registrado_group(sender, instance, created, **kwargs):
    if created:
        try:
            registrado = Group.objects.get(name='registrado')
        except Group.DoesNotExist:
            registrado = Group.objects.create(name='registrado')
            registrado = Group.objects.create(name= 'colaborador')
            registrado = Group.objects.create(name= '')
        instance.user.groups.add(registrado)



