from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    '''
    Profile model that has a one to one relationship with the user
    This ensures only one profile can be uploaded per user
    Uses CASCADE to ensure the profile is deleted if the user is deleted
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
