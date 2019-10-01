from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone
import datetime


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    description = models.TextField()
    education = models.CharField(max_length=100)
    fun_fact = models.TextField()
    image = models.ImageField(upload_to='profile_image/', blank=True)
    zip_code = models.CharField(max_length=5, default="")


    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)