from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import profile_photo

@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        # If the user is created, create a corresponding profile_photo instance
        profile_photo.objects.create(user=instance)
    else:
        # If the user is not created, attempt to update the associated profile_photo instance
        try:
            profile_photo_instance = profile_photo.objects.get(user=instance)
            # profile_photo_instance.address = instance.profile_photo.address
            # profile_photo_instance.phone = instance.profile_photo.phone
            # profile_photo_instance.image = instance.profile_photo.image
            # profile_photo_instance.Name = instance.profile_photo.Name
            profile_photo_instance.save()

        except profile_photo.DoesNotExist:
            # If the profile_photo doesn't exist, create a new one
            profile_photo.objects.create(user=instance)
