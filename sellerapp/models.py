from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to='seller_profile', null=True, blank=True)
    bio = models.TextField(blank=True, null=True, default="")
    location = models.CharField(max_length=255, blank=True, null=True)
    background_image = models.ImageField(upload_to='seller_backgrounds/', blank=True, null=True)

    def __str__(self):
        return self.user.username