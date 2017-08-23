from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User, related_name="profile")
    confirmed = models.BooleanField(default=False)
    alias = models.CharField(max_length=75, verbose_name="Username")
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    admin_comments = models.TextField(blank=True)
    fb_pic_path = models.CharField(max_length=120, null=True, blank=True)
    social_signup = models.CharField(max_length=10, blank=True, default='')
    closed = models.BooleanField(default=False)

