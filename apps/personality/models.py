from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_app.utils import get_default_dict

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=200, blank=True)
    balance = models.IntegerField(default=1000)
    avatar = models.ImageField(upload_to='images/avatars/', default='images/avatars/avatar.jpeg')
    monster_counter = models.JSONField(default=get_default_dict, blank=True)

    def __str__(self) -> str:
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()