from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

# class CustomUserManager()

class User(AbstractUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100,unique =True )
    bio = models.TextField(blank=True)
    phone_no = models.CharField(max_length = 10, null=True, blank=True)
    profile_pic = models.ImageField(upload_to="profile/", blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    
    def get_absolute_url(self):
        return reverse("account_detail", kwargs={"pk": self.pk})
    
    
    def __str__(self):
        return self.email if not self.username else self.username
    


