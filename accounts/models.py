from django.db import models
from django.contrib.auth.models import User
# import django signals
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to="profile/", blank=True, null=True)
    bio = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    join_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, **kwargs):
    # if a user already exist and has no profile created
    Profile.objects.get_or_create(user=instance)
