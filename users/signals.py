# for every user is created, a profile is automatically created 
# with default profile picture

from django.db.models.signals import post_save
# signal fired once object is saved

from django.contrib.auth.models import User
# sending signals

from django.dispatch import receiver
#receiving signals

from .models import Profile

#everytime user is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        #user_created
        Profile.objects.create(user=instance)


#save profile everytime user is created
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()