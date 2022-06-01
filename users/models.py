from django.db import models
from django.contrib.auth.models import User


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(upload_to='profile_images', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def _str_(self):
        return self.user