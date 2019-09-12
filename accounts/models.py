from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    '''
    Profile model that has a one to one relationship with the user
    This ensures only one profile can be uploaded per user
    Uses CASCADE to ensure the profile is deleted if the user is deleted
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.png', upload_to='profile_pics')
    
    def __str__(self):
        return f"{self.user.username}'s Profile"


def create_profile(sender, instance, created, **kwargs):
    '''
    Creates a user profile when a new user is registered
    '''
    if created:
        Profile.objects.create(user=instance)


def save_profile(sender, instance, **kwargs):
    '''
    Saves the profile when User is updated/changed
    '''
    instance.profile.save()

post_save.connect(create_profile, sender=User)
