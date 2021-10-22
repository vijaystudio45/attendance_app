from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('hr', '1'),
        ('employee', '2'),
    )
    first_name = models.CharField(max_length=250)
    email = models.EmailField(_('email address'), unique=True)
    last_name = models.CharField(max_length=250)
    username = models.CharField(max_length=250, null=True, blank=True)
    status = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=None, null=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()



class Employee_attendance_Model(models.Model):
    user_id = models.TextField(blank=True, null=True)
    start_date = models.TextField(blank=True, null=True)
    start_time = models.TextField(blank=True, null=True)
    end_date = models.TextField(blank=True, null=True)
    end_time = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now=True)
